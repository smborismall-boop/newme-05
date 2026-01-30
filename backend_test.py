#!/usr/bin/env python3

import requests
import sys
import json
from datetime import datetime
import time

class NewmeClassAPITester:
    def __init__(self, base_url="https://website-launch-6.preview.emergentagent.com"):
        self.base_url = base_url
        self.token = None
        self.tests_run = 0
        self.tests_passed = 0
        self.test_results = []

    def log_test(self, name, success, details=""):
        """Log test result"""
        self.tests_run += 1
        if success:
            self.tests_passed += 1
        
        result = {
            "test": name,
            "success": success,
            "details": details,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.test_results.append(result)
        
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {name}")
        if details:
            print(f"    Details: {details}")

    def run_api_test(self, name, method, endpoint, expected_status, data=None, headers=None):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        
        # Default headers
        default_headers = {'Content-Type': 'application/json'}
        if self.token:
            default_headers['Authorization'] = f'Bearer {self.token}'
        
        if headers:
            default_headers.update(headers)

        print(f"\n🔍 Testing {name}...")
        print(f"   URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=default_headers, timeout=30)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=default_headers, timeout=30)
            elif method == 'PUT':
                response = requests.put(url, json=data, headers=default_headers, timeout=30)
            elif method == 'DELETE':
                response = requests.delete(url, headers=default_headers, timeout=30)

            success = response.status_code == expected_status
            
            try:
                response_data = response.json()
            except:
                response_data = {"text": response.text[:200]}

            details = f"Status: {response.status_code}, Response: {json.dumps(response_data, indent=2)[:300]}"
            
            self.log_test(name, success, details)
            return success, response_data

        except requests.exceptions.Timeout:
            self.log_test(name, False, "Request timeout (30s)")
            return False, {}
        except requests.exceptions.ConnectionError:
            self.log_test(name, False, "Connection error - server may be down")
            return False, {}
        except Exception as e:
            self.log_test(name, False, f"Error: {str(e)}")
            return False, {}

    def test_health_check(self):
        """Test health endpoint"""
        return self.run_api_test(
            "Health Check",
            "GET",
            "api/health",
            200
        )

    def test_user_registration(self):
        """Test user registration"""
        test_user_data = {
            "email": f"testuser_{int(time.time())}@newmeclass.com",
            "password": "password123",
            "fullName": "Test User NEWME",
            "birthDate": "1990-01-01",
            "whatsapp": "081234567890",
            "userType": "individual",
            "referralSource": "google",  # Fixed: use valid enum value
            "province": "DKI Jakarta",
            "city": "Jakarta Selatan",
            "district": "Kebayoran Baru",
            "village": "Senayan",
            "address": "Jl. Test No. 123"
        }
        
        success, response = self.run_api_test(
            "User Registration",
            "POST",
            "api/auth/register",
            200,
            test_user_data
        )
        
        if success and response.get("token"):
            self.token = response["token"]
            print(f"    ✅ Got auth token: {self.token[:20]}...")
        
        return success, response

    def test_user_login(self):
        """Test user login with provided credentials"""
        login_data = {
            "email": "testuser@newmeclass.com",
            "password": "password123"
        }
        
        success, response = self.run_api_test(
            "User Login",
            "POST",
            "api/auth/login",
            200,
            login_data
        )
        
        if success and response.get("token"):
            self.token = response["token"]
            print(f"    ✅ Got auth token: {self.token[:20]}...")
        
        return success, response

    def test_get_all_questions(self):
        """Test GET /api/questions - should return all 40 questions"""
        success, response = self.run_api_test(
            "Get All Questions (40 total)",
            "GET",
            "api/questions",
            200
        )
        
        if success:
            questions = response if isinstance(response, list) else []
            count = len(questions)
            expected = 40
            
            if count == expected:
                print(f"    ✅ Correct count: {count} questions")
            else:
                print(f"    ⚠️  Expected {expected} questions, got {count}")
                success = False
        
        return success, response

    def test_get_free_questions(self):
        """Test GET /api/questions?testType=free - should return 5 free questions"""
        success, response = self.run_api_test(
            "Get Free Questions (5 expected)",
            "GET",
            "api/questions?testType=free",
            200
        )
        
        if success:
            questions = response if isinstance(response, list) else []
            count = len(questions)
            expected = 5
            
            if count == expected:
                print(f"    ✅ Correct count: {count} free questions")
                # Check if all are marked as free
                free_count = sum(1 for q in questions if q.get("testType") == "free" or q.get("isFree") == True)
                if free_count == count:
                    print(f"    ✅ All questions correctly marked as free")
                else:
                    print(f"    ⚠️  Only {free_count}/{count} questions marked as free")
            else:
                print(f"    ⚠️  Expected {expected} free questions, got {count}")
                success = False
        
        return success, response

    def test_get_paid_questions(self):
        """Test GET /api/questions?testType=paid - should return 35 paid questions"""
        success, response = self.run_api_test(
            "Get Paid Questions (35 expected)",
            "GET",
            "api/questions?testType=paid",
            200
        )
        
        if success:
            questions = response if isinstance(response, list) else []
            count = len(questions)
            expected = 35
            
            if count == expected:
                print(f"    ✅ Correct count: {count} paid questions")
                # Check if all are marked as paid
                paid_count = sum(1 for q in questions if q.get("testType") == "paid" or q.get("isFree") == False)
                if paid_count == count:
                    print(f"    ✅ All questions correctly marked as paid")
                else:
                    print(f"    ⚠️  Only {paid_count}/{count} questions marked as paid")
            else:
                print(f"    ⚠️  Expected {expected} paid questions, got {count}")
                success = False
        
        return success, response

    def test_certificate_eligibility(self):
        """Test certificate eligibility check"""
        if not self.token:
            print("    ⚠️  Skipping certificate test - no auth token")
            return False, {}
        
        return self.run_api_test(
            "Certificate Eligibility Check",
            "GET",
            "api/certificates/check-eligibility",
            200
        )

    def test_ai_analysis_endpoint(self):
        """Test AI analysis endpoint (requires auth)"""
        if not self.token:
            print("    ⚠️  Skipping AI analysis test - no auth token")
            return False, {}
        
        # Sample test data for AI analysis
        test_analysis_data = {
            "testType": "free",
            "answers": [
                {
                    "questionId": "test123",
                    "questionText": "Test question",
                    "category": "personality",
                    "answer": "Test answer",
                    "score": 3
                }
            ],
            "categoryScores": {
                "personality": {"score": 15, "max": 20}
            },
            "totalScore": 15,
            "maxScore": 20,
            "percentage": 75
        }
        
        return self.run_api_test(
            "AI Analysis Endpoint",
            "POST",
            "api/ai-analysis/analyze",
            200,
            test_analysis_data
        )

    def run_all_tests(self):
        """Run all API tests"""
        print("🚀 Starting NEWME CLASS API Tests")
        print("=" * 50)
        
        # Basic health check
        self.test_health_check()
        
        # Authentication tests
        reg_success, reg_response = self.test_user_registration()
        if not reg_success:
            # Try login with existing user if registration fails
            self.test_user_login()
        
        # Questions API tests
        self.test_get_all_questions()
        self.test_get_free_questions()
        self.test_get_paid_questions()
        
        # Certificate tests
        self.test_certificate_eligibility()
        
        # AI Analysis test
        self.test_ai_analysis_endpoint()
        
        # Print summary
        print("\n" + "=" * 50)
        print("📊 TEST SUMMARY")
        print("=" * 50)
        print(f"Total Tests: {self.tests_run}")
        print(f"Passed: {self.tests_passed}")
        print(f"Failed: {self.tests_run - self.tests_passed}")
        print(f"Success Rate: {(self.tests_passed/self.tests_run*100):.1f}%")
        
        # Print failed tests
        failed_tests = [r for r in self.test_results if not r["success"]]
        if failed_tests:
            print("\n❌ FAILED TESTS:")
            for test in failed_tests:
                print(f"  - {test['test']}: {test['details']}")
        
        return self.tests_passed == self.tests_run

def main():
    """Main test runner"""
    tester = NewmeClassAPITester()
    
    try:
        success = tester.run_all_tests()
        return 0 if success else 1
    except KeyboardInterrupt:
        print("\n⚠️  Tests interrupted by user")
        return 1
    except Exception as e:
        print(f"\n💥 Unexpected error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())