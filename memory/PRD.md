# NEWMECLASS Website - PRD

## Original Problem Statement
Deploy website dari GitHub: https://github.com/smborismall-boop/newme-03
Updates:
- Fix pertanyaan gratis dan berbayar (5 gratis + 35 berbayar = 40 total)
- Include AI analyst lengkap dengan 9 hasil berbeda
- Fitur download sertifikat dengan design baru
- Element ANGIN diganti LOGAM
- Fix: user sudah bayar tapi masih keluar notif saldo tidak cukup
- Test gratis hanya bisa dilakukan sekali per user
- Harga test premium dapat diubah di admin dashboard

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
- AI Analysis menggunakan GPT-4o dengan 9 hasil berbeda
- Sistem wallet untuk pembayaran
- Sertifikat digital untuk test berbayar
- Harga test dapat diubah dari admin dashboard

## 9 Kategori Hasil Test
1. **eK** - EXTROVERT-KAYU (Si Kreatif Ekspresif)
2. **eA** - EXTROVERT-API (Si Perasa Hangat)
3. **eT** - EXTROVERT-TANAH (Si Stabil Terbuka)
4. **iK** - INTROVERT-KAYU (Si Kreatif Mendalam)
5. **iA** - INTROVERT-API (Si Perasa Dalam)
6. **iT** - INTROVERT-TANAH (Si Stabil Tenang)
7. **aL** - AMBIVERT-LOGAM (Si Tegas Seimbang)
8. **aAi** - AMBIVERT-AIR (Si Adaptif Seimbang)
9. **aT** - AMBIVERT-TANAH (Si Stabil Fleksibel)

## What's Been Implemented

### Feb 5, 2026 - Latest Updates:
1. **9 Hasil Berbeda** - AI Analysis dengan 9 kategori hasil berdasarkan kombinasi kepribadian + element
2. **Certificate Design** - Template sertifikat sesuai design yang diberikan
3. **Test Price Management** - Admin dapat mengubah harga test dari Settings
4. **Free Test Tracking** - User hanya bisa mengambil test gratis 1x
5. **Payment Status Fix** - Pengecekan status pembayaran diperbaiki
6. **Element Update** - ANGIN → LOGAM (SI TEGAS)

### Jan 30, 2026:
- Repository cloned & deployed from GitHub
- Questions seeded: 5 gratis + 35 berbayar = 40 total
- AI Analysis integrated with GPT-4o

### API Endpoints:
- `GET /api/settings/test-price` - Get test price
- `PUT /api/settings/test-price` - Update test price (admin)
- `GET /api/user-payments/status/{userId}` - Check payment status
- `GET /api/test-results/check-free-test/{userId}` - Check free test usage

## Testing Status
- **Backend**: 100% passed
- **Frontend**: 100% working
- **Admin Dashboard**: Price management working

## Credentials
- Admin: admin@newmeclass.com / admin123
- User: testuser@newmeclass.com / password123

## Mocked APIs
- **Midtrans QRIS Payment** - demo-topup endpoint

## Prioritized Backlog

### P0 (Critical) - DONE ✅
- [x] 9 hasil berbeda berdasarkan kepribadian + element
- [x] Harga test dapat diubah di admin
- [x] Free test hanya 1x per user
- [x] Payment status fix

### P1 (High Priority)
- [ ] Real Midtrans payment integration
- [ ] Certificate PDF download with new design

### P2 (Medium Priority)
- [ ] Admin dashboard improvements
- [ ] Partner logos carousel

## Next Tasks
1. Integrate real Midtrans payment
2. Generate PDF certificate with template design
