import os

project_dir = "/home/zeraa/projects/blocs"
os.makedirs(os.path.join(project_dir, "src/pages"), exist_ok=True)
os.makedirs(os.path.join(project_dir, "src/components"), exist_ok=True)
os.makedirs(os.path.join(project_dir, "src/layouts"), exist_ok=True)

# 1. Package.json
pkg = """{
  "name": "konveksi-nusantara-luxury",
  "type": "module",
  "version": "1.0.0",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  },
  "dependencies": {
    "astro": "^4.0.0"
  }
}"""
with open(os.path.join(project_dir, "package.json"), "w") as f:
    f.write(pkg)

# 2. Astro Config
astro_config = """import { defineConfig } from 'astro/config';
export default defineConfig({});
"""
with open(os.path.join(project_dir, "astro.config.mjs"), "w") as f:
    f.write(astro_config)

# 3. Main Layout with Luxury Styling (Instrument Serif + Plus Jakarta Sans, Smooth Scroll, Custom Animations)
layout = """---
const { title = "Konveksi Nusantara — Luxury Garment & Apparel Solution" } = Astro.props;
---
<!DOCTYPE html>
<html lang="id" class="light scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        .font-serif {
            font-family: 'Instrument Serif', serif;
        }
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        .animate-float {
            animation: float 4s ease-in-out infinite;
        }
        @keyframes marquee {
            0% { transform: translateX(0%); }
            100% { transform: translateX(-50%); }
        }
        .animate-marquee {
            display: flex;
            width: 200%;
            animation: marquee 25s linear infinite;
        }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body class="bg-[#faf9f6] text-neutral-900 selection:bg-neutral-900 selection:text-white antialiased overflow-x-hidden">
    <!-- Navbar -->
    <header class="fixed top-0 inset-x-0 z-50 bg-[#faf9f6]/80 backdrop-blur-md border-b border-neutral-200/60 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
            <a href="/" class="flex items-center gap-2 group">
                <span class="font-serif text-3xl tracking-wide text-neutral-900 group-hover:opacity-80 transition-opacity">KONVEKSI<span class="text-amber-700">.</span></span>
            </a>
            <nav class="hidden md:flex items-center gap-10 text-sm font-medium text-neutral-600">
                <a href="/" class="hover:text-neutral-900 transition-colors">Beranda</a>
                <a href="/about" class="hover:text-neutral-900 transition-colors">Tentang Kami</a>
                <a href="/katalog" class="hover:text-neutral-900 transition-colors">Katalog Produk</a>
                <a href="/galeri" class="hover:text-neutral-900 transition-colors">Galeri & Testimoni</a>
            </nav>
            <div class="flex items-center gap-4">
                <a href="https://wa.me/6281234567890" target="_blank" class="px-6 py-2.5 rounded-full bg-neutral-900 text-white text-xs font-semibold tracking-wider uppercase hover:bg-neutral-800 transition-all shadow-md hover:shadow-lg active:scale-95">
                    Konsultasi VIP
                </a>
            </div>
        </div>
    </header>

    <main class="pt-20">
        <slot />
    </main>

    <!-- Footer -->
    <footer class="bg-neutral-900 text-neutral-400 py-16 px-6 border-t border-neutral-800">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-12 mb-16">
            <div class="space-y-4">
                <span class="font-serif text-3xl text-white tracking-wide">KONVEKSI<span class="text-amber-500">.</span></span>
                <p class="text-sm font-light leading-relaxed text-neutral-400">Pabrik manufaktur pakaian & garment mewah berstandar internasional dengan presisi tinggi dan komitmen tanpa kompromi.</p>
            </div>
            <div>
                <h4 class="text-white text-sm font-semibold tracking-wider uppercase mb-4">Navigasi Cepat</h4>
                <ul class="space-y-2.5 text-sm font-light">
                    <li><a href="/" class="hover:text-white transition-colors">Beranda Utama</a></li>
                    <li><a href="/about" class="hover:text-white transition-colors">Visi & Misi Perusahaan</a></li>
                    <li><a href="/katalog" class="hover:text-white transition-colors">20+ Katalog Produk</a></li>
                    <li><a href="/galeri" class="hover:text-white transition-colors">Galeri & 10 Testimoni Klien</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white text-sm font-semibold tracking-wider uppercase mb-4">Pusat Produksi</h4>
                <p class="text-sm font-light leading-relaxed">Kawasan Industri Garment Blok C-12, Jakarta Timur, Indonesia.</p>
                <p class="text-sm font-light mt-4 text-white font-medium">support@konveksinusantara.luxury</p>
            </div>
            <div>
                <h4 class="text-white text-sm font-semibold tracking-wider uppercase mb-4">Simulasi Sistem Admin</h4>
                <p class="text-sm font-light mb-4 text-neutral-400">Akses panel kontrol manajemen produksi dan inventaris berbasis Filament.</p>
                <a href="#admin-login" onclick="alert('Mengarahkan ke Filament Admin Panel v3...'); return false;" class="inline-block px-5 py-2.5 bg-amber-600 text-white text-xs font-semibold rounded-lg hover:bg-amber-500 transition-colors shadow">
                    Masuk Admin Filament ⚡
                </a>
            </div>
        </div>
        <div class="max-w-7xl mx-auto pt-8 border-t border-neutral-800 flex flex-col sm:flex-row items-center justify-between text-xs font-light">
            <p>&copy; 2026 PT Konveksi Nusantara Luxury. All rights reserved.</p>
            <div class="flex gap-6 mt-4 sm:mt-0">
                <span>Privacy Policy</span>
                <span>Terms of Service</span>
                <span>ISO 9001:2015 Certified</span>
            </div>
        </div>
    </footer>
</body>
</html>
"""
with open(os.path.join(project_dir, "src/layouts/Layout.astro"), "w") as f:
    f.write(layout)

# 4. Component: Luxury Hero Section for Beranda
hero_component = """---
---
<section class="relative min-h-[90vh] flex flex-col justify-center bg-[#faf9f6] px-6 py-12 overflow-hidden" x-data="{
    activeSlide: 0,
    typedText: '',
    slides: [
        { title: 'jaket custom mewah?', desc: 'Eksklusif dengan bahan waterproof pilihan & jahitan presisi.', img: 'https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&q=80&w=900' },
        { title: 'hoodie & sweater premium?', desc: 'Kenyamanan maksimal dengan cotton fleece tebal anti-bulu.', img: 'https://images.unsplash.com/photo-1556905055-8f358a7a47b2?auto=format&fit=crop&q=80&w=900' },
        { title: 'seragam PDH eksekutif?', desc: 'Tampilan berwibawa dan elegan untuk korporat & instansi.', img: 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&q=80&w=900' },
        { title: 'kaos sablon high-end?', desc: 'Cotton combed 24s reactive dengan cetak plastisol & DTF tajam.', img: 'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&q=80&w=900' },
        { title: 'jas almamater universitas?', desc: 'Simbol kebanggaan kampus dengan furing penuh berkualitas tinggi.', img: 'https://images.unsplash.com/photo-1594938298603-c8148c4dae35?auto=format&fit=crop&q=80&w=900' }
    ],
    async typeText(text) {
        while (this.typedText.length > 0) {
            this.typedText = this.typedText.slice(0, -1);
            await new Promise(r => setTimeout(r, 30));
        }
        for (let i = 0; i < text.length; i++) {
            this.typedText += text.charAt(i);
            await new Promise(r => setTimeout(r, 50));
        }
    },
    init() {
        this.typedText = this.slides[0].title;
        setInterval(async () => {
            this.activeSlide = (this.activeSlide + 1) % this.slides.length;
            await this.typeText(this.slides[this.activeSlide].title);
        }, 3200);
    }
}">
    <!-- Background Luxury Glow Elements -->
    <div class="absolute top-1/4 left-1/4 w-96 h-96 bg-amber-200/20 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute bottom-1/4 right-1/4 w-96 h-96 bg-neutral-300/20 rounded-full blur-3xl pointer-events-none"></div>

    <div class="relative z-10 max-w-7xl mx-auto w-full grid grid-cols-1 lg:grid-cols-12 gap-12 items-center py-12">
        <div class="lg:col-span-6 flex flex-col items-start text-left">
            <div class="inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full bg-neutral-200/70 border border-neutral-300 text-xs font-semibold tracking-wider text-neutral-800 mb-6 uppercase">
                <span class="w-2 h-2 rounded-full bg-amber-600 animate-ping"></span>
                <span>Manufaktur Garment Kelas Dunia</span>
            </div>

            <h1 class="text-4xl sm:text-6xl lg:text-7xl font-light tracking-tight text-neutral-900 mb-6 leading-[1.1]">
                Pengen mau buat <br />
                <span class="font-serif italic text-amber-900 font-normal">
                    <span x-text="typedText"></span><span class="inline-block w-[3px] h-[0.85em] bg-neutral-900 ml-1 align-middle" style="animation: blink 0.8s infinite;"></span>
                </span>
            </h1>

            <style>
                @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
            </style>

            <p class="max-w-xl text-lg text-neutral-600 font-light mb-10 leading-relaxed" x-text="slides[activeSlide].desc">
                Wujudkan standar pakaian impian Anda bersama pabrik konveksi mewah bersertifikasi internasional.
            </p>

            <div class="flex flex-col sm:flex-row items-center gap-4 w-full sm:w-auto">
                <a href="/katalog" class="w-full sm:w-auto px-8 py-4 rounded-full bg-neutral-900 text-white font-medium text-sm tracking-wide hover:bg-neutral-800 transition-all text-center shadow-lg hover:shadow-xl">
                    Jelajahi 20+ Katalog Produk
                </a>
                <a href="/about" class="w-full sm:w-auto px-8 py-4 rounded-full bg-white border border-neutral-300 text-neutral-900 font-medium text-sm tracking-wide hover:bg-neutral-100 transition-all text-center">
                    Tentang Perusahaan
                </a>
            </div>
        </div>

        <!-- Carousel Apparel Image with Blur Side Gradients -->
        <div class="lg:col-span-6 relative flex items-center justify-center">
            <div class="absolute left-0 inset-y-0 w-24 bg-gradient-to-r from-[#faf9f6] via-[#faf9f6]/80 to-transparent z-10 pointer-events-none"></div>
            <div class="absolute right-0 inset-y-0 w-24 bg-gradient-to-l from-[#faf9f6] via-[#faf9f6]/80 to-transparent z-10 pointer-events-none"></div>

            <div class="w-full overflow-hidden relative py-6">
                <div class="flex transition-transform duration-700 ease-in-out items-center" :style="`transform: translateX(-${activeSlide * 100}%)`">
                    <template x-for="(slide, index) in slides" :key="index">
                        <div class="w-full flex-shrink-0 flex items-center justify-center px-8 animate-float">
                            <img :src="slide.img" :alt="slide.title" class="max-h-[420px] w-auto object-contain drop-shadow-2xl mix-blend-multiply" />
                        </div>
                    </template>
                </div>
            </div>
        </div>
    </div>
</section>
"""
with open(os.path.join(project_dir, "src/components/Hero.astro"), "w") as f:
    f.write(hero_component)

print("Luxury site foundation created successfully!")
