# NEWMECLASS Website - PRD

## Original Problem Statement
Deploy website dari GitHub: https://github.com/smborismall-boop/newme-03
Kemudian fix: pertanyaan gratis dan berbayar belum muncul, tambahkan pertanyaan berbayar menjadi 35, include AI analyst lengkap dan fitur download sertifikat.

## Architecture & Tech Stack
- **Frontend**: React.js with Tailwind CSS + Shadcn UI
- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **AI Integration**: GPT-4o via Emergent LLM Key

## User Personas
1. **Siswa/Mahasiswa** - mencari test kepribadian dan bakat
2. **Korporasi/Yayasan** - mencari program pelatihan B2B
3. **Individual** - mencari konseling dan pengembangan diri

## Core Requirements (Static)
- Website company profile untuk NEWMECLASS
- Slider/carousel untuk menampilkan informasi perusahaan
- Test kepribadian (gratis & berbayar)
- AI Analysis menggunakan GPT-4o
- Sistem wallet untuk pembayaran
- Sertifikat digital untuk test berbayar

## What's Been Implemented

### Jan 30, 2026 - Latest Updates:
1. **Repository Cloned & Deployed** from GitHub
2. **Questions System Updated** - 40 pertanyaan total:
   - 5 pertanyaan GRATIS
   - 35 pertanyaan BERBAYAR
3. **AI Analysis Integrated** - GPT-4o via Emergent LLM Key
   - Analisis kepribadian 5 ELEMENT (KAYU, API, TANAH, ANGIN, AIR)
   - INTROVERT/EXTROVERT/AMBIVERT detection
   - Detailed career recommendations
4. **Certificate Download** - PDF generation for paid users
   - 2-page certificate with detailed analysis
   - Formatted like NEWME CLASS official template
5. **Test Credentials Created**:
   - Email: testuser@newmeclass.com
   - Password: password123

### API Endpoints Working:
- `GET /api/questions` - All 40 questions
- `GET /api/questions?testType=free` - 5 free questions
- `GET /api/questions?testType=paid` - 35 paid questions
- `POST /api/ai-analysis/analyze` - AI-powered analysis
- `GET /api/certificates/check-eligibility` - Check download eligibility
- `GET /api/certificates/download-ai-certificate` - Download PDF certificate

## Testing Status
- **Backend**: 100% passed (questions, auth, certificates API)
- **Frontend**: 100% working (carousel, forms, navigation)

## Mocked APIs
- **Midtrans QRIS Payment** - demo-topup endpoint simulates payment without real integration

## Prioritized Backlog

### P0 (Critical) - DONE ✅
- [x] Clone & deploy from GitHub
- [x] Questions system (5 free + 35 paid = 40 total)
- [x] AI Analysis integration with GPT-4o
- [x] Certificate download for paid users
- [x] User registration & login

### P1 (High Priority) - Pending
- [ ] Real Midtrans QRIS payment integration
- [ ] Admin dashboard improvements

### P2 (Medium Priority)
- [ ] Partner logos carousel
- [ ] Animation improvements

## Next Tasks
1. User dapat melakukan test gratis dan mendapat hasil dasar
2. Upgrade ke test berbayar untuk analisis AI lengkap
3. Download sertifikat setelah pembayaran disetujui
