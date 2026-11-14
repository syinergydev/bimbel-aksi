import os, json, urllib.parse as up
OUT = '/home/claude/aksi_site'
SITE = 'https://example.com'  # ganti dengan domain final
# ---------- DATA TERPUSAT (edit di sini) ----------
B = dict(name='Bimbel AKSI', full='Bimbingan Belajar AKSI', tag='Belajar Ceria, Berkembang Bersama!',
 wa='628563305025', wad='0856-3305-025', mail='bimbinganbelajaraksi@gmail.com',
 ig='https://www.instagram.com/bimbel.aksi', igh='@bimbel.aksi', tt='https://www.tiktok.com/@bimbel.aksi123', tth='@bimbel.aksi123',
 map='https://maps.app.goo.gl/pmybYHiky3W4Xg486', rating='5,0', rev=50,
 addr='Jl. Balai Desa Blok 3, RT.04/RW.03, Dusun Ganting, Ganting, Kec. Gedangan, Kabupaten Sidoarjo, Jawa Timur 61254.')
REV = ['Ananda jadi lebih bersemangat belajarnya, karena di-mentor-i dengan guru-guru hebat.',
 'Tempat bimbingan belajar yang sangat nyaman, pembelajaran yang menyenangkan dengan kualitas yang sangat patut diacungi jempol.',
 'Tempat bimbel yang dekat dari rumah, guru yang berpengalaman, anak-anak mudah memahami materi dibimbing dengan sabar.']
SUBJ = [('Bahasa Indonesia', 'book'), ('Bahasa Inggris', 'globe'), ('Matematika', 'calc'), ('IPAS', 'flask')]
NOTE = 'Jadwal, biaya, dan ketersediaan kelas dapat berubah. Tanyakan informasi terbaru melalui WhatsApp.'
GAL = [('papan-tulis', 'Anak berlatih berhitung di papan tulis', 'calistung', 'wide'), ('calistung-1', 'Anak mengerjakan kegiatan belajar di papan warna', 'calistung', 'tall'),
 ('belajar-1', 'Anak-anak belajar di meja lipat', 'calistung', 'tall'), ('kelas-1', 'Suasana kelas dengan anak-anak belajar bersama', 'belajar', 'tall'),
 ('kelas-2', 'Kelas dengan meja lipat dan karpet', 'belajar', 'tall'), ('kelas-3', 'Ruang belajar dengan dinding berwarna', 'belajar', 'wide'),
 ('dinding', 'Dinding ruang belajar bergambar pelangi dan logo AKSI', 'belajar', 'wide'), ('kelompok-1', 'Pembelajaran kelompok dengan modul', 'kelompok', 'tall'),
 ('kelompok-2', 'Anak belajar bersama pendamping', 'kelompok', 'wide'), ('meja-anak', 'Anak-anak mengerjakan tugas di meja', 'kelompok', 'wide'),
 ('aktivitas-1', 'Aktivitas anak duduk bersama di luar ruangan', 'aktivitas', 'wide'), ('aktivitas-2', 'Kegiatan siswa di luar ruangan', 'aktivitas', 'tall'),
 ('luar-pohon', 'Kegiatan belajar di luar kelas', 'luar', 'tall'), ('luar-duduk', 'Anak-anak duduk melingkar di luar kelas', 'luar', 'wide'),
 ('bersama', 'Dokumentasi bersama siswa di depan dinding AKSI', 'bersama', 'tall')]
CATS = [('semua', 'Semua'), ('belajar', 'Kegiatan belajar'), ('calistung', 'Calistung'), ('kelompok', 'Belajar kelompok'), ('aktivitas', 'Aktivitas siswa'), ('luar', 'Luar kelas'), ('bersama', 'Dokumentasi bersama')]
PR = [
 dict(slug='calistung', n='Calistung', lv='Mulai usia 4 tahun (informasi Maps)', d='Belajar membaca, menulis, dan berhitung secara bertahap dengan buku modul Calistung.', img='papan-tulis',
  tgt='Anak yang mulai belajar membaca, menulis, dan berhitung, mulai usia 4 tahun.', mat=['Membaca', 'Menulis', 'Berhitung', 'Buku modul Calistung'], adv=['Pembelajaran bertahap dengan modul', 'Suasana belajar yang menyenangkan', 'Pendamping yang sabar (berdasarkan ulasan Google Maps)']),
 dict(slug='bimbingan-sd', n='Bimbingan Belajar SD', lv='Siswa SD kelas 1–5', d='Pendampingan pelajaran sekolah, pengerjaan PR, dan evaluasi perkembangan belajar.', img='kelas-2',
  tgt='Siswa SD kelas 1–5. Kelas 6 memiliki perlakuan khusus dan perlu dikonsultasikan.', mat=['Bahasa Indonesia', 'Bahasa Inggris', 'Matematika', 'IPAS', 'Bimbingan pengerjaan PR'], adv=['Mengikuti kurikulum sekolah', 'Modul pembelajaran', 'Evaluasi perkembangan belajar'])]
SUPPORT = [('Asesmen diagnostik', 'search'), ('Evaluasi & pelaporan perkembangan', 'chart'), ('Ujian akhir tingkat', 'check'), ('Ujian kenaikan tingkat', 'check'), ('Game edukasi', 'star'), ('Kegiatan belajar di luar kelas', 'sun')]
MODUL = [('Modul membaca', 'Seri “Saya Pandai Baca” untuk berlatih membaca.'), ('Modul berhitung', 'Seri “Saya Pintar Berhitung” untuk berlatih berhitung.'), ('Modul Calistung', 'Materi pendamping program Calistung.'), ('Modul Matematika', 'Materi pendamping bimbingan belajar SD.'), ('Modul Bahasa Inggris', 'Materi pendamping Bahasa Inggris.'), ('Merchandise Bimbel AKSI', 'Kaos dan perlengkapan bertema AKSI.')]
FAQ = [('Mulai usia berapa anak bisa ikut Calistung?', 'Berdasarkan informasi di Google Maps, Calistung dimulai dari usia 4 tahun. Konsultasikan kesiapan anak Anda lewat WhatsApp.'),
 ('Kelas SD berapa saja yang dilayani?', 'Bimbingan belajar SD untuk kelas 1–5. Kelas 6 memiliki perlakuan khusus, jadi silakan konsultasi dulu.'),
 ('Berapa biaya dan jadwal terbarunya?', 'Biaya dan jadwal tidak ditampilkan di sini karena dapat berubah. Tanyakan langsung melalui WhatsApp.'),
 ('Apakah anak dijamin bisa membaca dalam waktu tertentu?', 'Tidak ada jaminan waktu. Setiap anak berkembang dengan kecepatannya masing-masing, dan Bimbel AKSI mendampingi prosesnya.')]

# ---------- ICONS ----------
IC = {'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>', 'check': '<path d="M5 12.5l4.5 4.5L19 7.5"/>', 'plus': '<path d="M12 5v14M5 12h14"/>', 'x': '<path d="M6 6l12 12M18 6L6 18"/>', 'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>', 'chev': '<path d="M6 9l6 6 6-6"/>', 'play': '<path d="M8 5l11 7-11 7z"/>',
 'pin': '<path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>', 'star': '<path d="M12 3l2.7 5.6 6.1.8-4.5 4.2 1.1 6-5.4-3-5.4 3 1.1-6L3.2 9.4l6.1-.8z"/>',
 'wa': '<path d="M3 21l1.6-4.8A8.5 8.5 0 1 1 8 19.6L3 21z"/><path d="M9 9.5c.5 2.5 2.5 4.5 5 5l1.2-1.2-2-1-.8.8a4 4 0 0 1-1.8-1.8l.8-.8-1-2L9 9.5z"/>',
 'ig': '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".6"/>', 'tt': '<path d="M14 3v11.2a3.7 3.7 0 1 1-3.7-3.7"/><path d="M14 3c.3 2.5 2 4.2 4.7 4.5"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M4 7.5l8 6 8-6"/>',
 'book': '<path d="M4 5.5C7 4.5 10 4.8 12 6.5c2-1.7 5-2 8-1v13c-3-1-6-.7-8 1-2-1.700-5-2-8-1z"/><path d="M12 6.5v13"/>', 'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
 'calc': '<rect x="5" y="3" width="14" height="18" rx="3"/><path d="M8.500 7.500h7M8.500 12h1M12 12h1M15.500 12h0M8.500 16h1M12 16h1M15.500 16h0"/>', 'flask': '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.800 3h10.400a2 2 0 0 0 1.800-3l-5-9V3"/><path d="M7.500 15h9"/>',
 'search': '<circle cx="11" cy="11" r="6.500"/><path d="M16 16l4.500 4.500"/>', 'chart': '<path d="M4 20V4M4 20h16M8 16v-4M12 16V8M16 16v-6"/>', 'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
 'pen': '<path d="M4 20l1-4L16.500 4.500a2 2 0 0 1 3 3L8 19z"/>', 'abc': '<path d="M4 18l4-12 4 12M5.500 14h5M15 6v12M15 8c4-1 5 3 0 4c5 1 4 6 0 6"/>'}
def ic(n, c='ic'): return f'<svg class="{c}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{IC[n]}</svg>'
SOC = {'wa': ('#25D366', 'WhatsApp'), 'ig': ('#E1306C', 'Instagram'), 'tt': ('#111111', 'TikTok'), 'mail': ('#D8232A', 'Email'), 'pin': ('#2FA866', 'Google Maps')}
def soc(n, href, size=44, ext=True):
    bg, label = SOC[n]; t = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="soc" style="--b:{bg};--s:{size}px" href="{href}"{t} aria-label="{label} Bimbel AKSI">{ic(n)}</a>'
def write_soc():
    for n, (bg, label) in SOC.items():
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96"><rect width="96" height="96" rx="24" fill="{bg}"/><g transform="translate(20 20) scale(2.3)" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{IC[n]}</g></svg>'
        open(f'{OUT}/assets/social/{n}.svg', 'w').write(svg)
def wa(msg=None): return f"https://wa.me/{B['wa']}" + ('?text=' + up.quote(msg) if msg else '')
def wam(t): return wa(f"Halo Bimbel AKSI, saya ingin bertanya mengenai {t}. Terima kasih.")
def embed(): return 'https://www.google.com/maps?q=' + up.quote('Bimbel AKSI ' + B['addr']) + '&output=embed'
def img(f, a, c='', lazy=True, w=1080, h=1080): return f'<img class="{c}" src="{{R}}assets/img/{f}.webp" alt="{a}" width="{w}" height="{h}"' + (' loading="lazy"' if lazy else '') + ' decoding="async">'
def ring():
    c = 276.46
    return f'<svg class="ring" viewBox="0 0 100 100" role="img" aria-label="Rating {B["rating"]} dari 5"><circle cx="50" cy="50" r="44" fill="none" stroke="#FFE7A8" stroke-width="9"/><circle cx="50" cy="50" r="44" fill="none" stroke="#D8232A" stroke-width="9" stroke-linecap="round" stroke-dasharray="{c} {c}" transform="rotate(-90 50 50)"/><text x="50" y="57" text-anchor="middle" class="rt">{B["rating"]}</text></svg>'
def stars(): return f'<span class="rate">{ic("star")}<b>{B["rating"]}</b> dari 5 · {B["rev"]} ulasan Google Maps</span>'

# ---------- LAYOUT ----------
def page(title, desc, body, depth, active='', og='papan-tulis'):
    R = '../' * depth
    L = lambda p: R + p + ('index.html' if p == '' or p.endswith('/') else '')
    dd = ''.join(f'<a href="{L("program/"+p["slug"]+"/")}">{p["n"]}</a>' for p in PR)
    def nav(h, lab, k, d=None):
        cur = ' aria-current="page"' if active == k else ''
        if not d: return f'<li><a class="nl" href="{h}"{cur}>{lab}</a></li>'
        return f'<li class="has-dd"><a class="nl" href="{h}"{cur}>{lab}</a><button class="ddb" aria-label="Buka submenu {lab}" aria-expanded="false">{ic("chev")}</button><div class="dd">{d}</div></li>'
    nv = ''.join([nav(L(''), 'Beranda', 'home'), nav(L('tentang/'), 'Tentang', 'tentang'), nav(L('program/'), 'Program', 'program', dd), nav(L('galeri/'), 'Galeri', 'galeri'), nav(L('modul/'), 'Modul', 'modul'), nav(L('testimoni/'), 'Testimoni', 'testimoni'), nav(L('kontak/'), 'Kontak', 'kontak')])
    fn = ''.join(f'<li><a href="{L(p)}">{t}</a></li>' for p, t in [('', 'Beranda'), ('tentang/', 'Tentang'), ('galeri/', 'Galeri'), ('modul/', 'Modul'), ('testimoni/', 'Testimoni'), ('pendaftaran/', 'Konsultasi'), ('kontak/', 'Kontak')])
    fp = ''.join(f'<li><a href="{L("program/"+p["slug"]+"/")}">{p["n"]}</a></li>' for p in PR)
    ld = json.dumps({"@context": "https://schema.org", "@type": "EducationalOrganization", "name": B['full'], "telephone": '+' + B['wa'], "email": B['mail'], "address": {"@type": "PostalAddress", "streetAddress": B['addr'], "addressLocality": "Gedangan", "addressRegion": "Jawa Timur", "addressCountry": "ID"}, "hasMap": B['map'], "sameAs": [B['ig'], B['tt']]}, ensure_ascii=False)
    return f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:locale" content="id_ID"><meta property="og:image" content="{SITE}/assets/img/{og}.webp">
<link rel="icon" href="{R}assets/img/favicon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&family=Nunito+Sans:wght@400;600;700&display=swap"><link rel="stylesheet" href="{R}assets/style.css"><script type="application/ld+json">{ld}</script></head><body>
<a class="skip" href="#main">Lewati ke konten</a>
<header class="hdr" id="hdr"><div class="wrap hdr-in"><a class="logo" href="{L('')}" aria-label="Bimbel AKSI – Beranda"><img src="{R}assets/img/logo-horizontal.jpg" alt="Bimbingan Belajar AKSI" width="170" height="38"></a>
<nav aria-label="Navigasi utama" id="nav"><ul>{nv}</ul></nav><a class="btn btn-r hdr-cta" href="{L('pendaftaran/')}">Konsultasi</a><button class="burger" id="burger" aria-label="Buka menu" aria-expanded="false" aria-controls="nav">{ic('menu')}</button></div></header>
<main id="main">{body}</main>
<footer class="ftr"><div class="wrap fg"><div><img class="flogo" src="{R}assets/img/logo-horizontal.jpg" alt="Bimbingan Belajar AKSI" width="170" height="38"><p>{B['tag']} Bimbingan Calistung dan belajar SD di Ganting, Gedangan, Sidoarjo.</p><div class="socs">{soc('wa', wa())}{soc('ig', B['ig'])}{soc('tt', B['tt'])}{soc('mail', 'mailto:'+B['mail'], ext=False)}{soc('pin', B['map'])}</div></div>
<div><h2>Navigasi</h2><ul>{fn}</ul></div><div><h2>Program</h2><ul>{fp}</ul></div>
<div><h2>Kontak</h2><ul><li><a href="{wa()}" target="_blank" rel="noopener">WhatsApp {B['wad']}</a></li><li><a href="mailto:{B['mail']}">{B['mail']}</a></li><li><a href="{B['ig']}" target="_blank" rel="noopener">Instagram {B['igh']}</a></li><li><a href="{B['tt']}" target="_blank" rel="noopener">TikTok {B['tth']}</a></li><li class="ad">{B['addr']}</li></ul></div></div>
<div class="wrap fb"><small>© 2026 {B['full']}. Situs ini adalah demo konsep; informasi akan diperbarui sesuai data resmi dari pengelola.</small></div></footer>
<a class="wafab" href="{wa('Halo Bimbel AKSI, saya ingin berkonsultasi mengenai program belajar.')}" target="_blank" rel="noopener" aria-label="Konsultasi via WhatsApp">{ic('wa')}<span>Konsultasi</span></a>
<script src="{R}assets/app.js" defer></script></body></html>'''.replace('{R}', R)
def write(p, h):
    d = os.path.join(OUT, p); os.makedirs(d, exist_ok=True); open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(h)
def phead(t, s, k=''): return f'<section class="phead"><div class="wrap"><h1 class="rv">{t}</h1><p class="lede rv">{s}</p></div></section>'
def cta(t='Ingin tahu program yang cocok untuk anak Anda?'):
    return f'<section class="sec"><div class="wrap"><div class="ctab rv"><div><h2>{t}</h2><p>Ceritakan usia dan kelas anak. Kami bantu jelaskan program, jadwal, dan biaya terbaru.</p></div><div class="acts"><a class="btn btn-y btn-l" href="{{R}}pendaftaran/index.html">Konsultasi Sekarang</a><a class="btn btn-w btn-l" href="{wa()}" target="_blank" rel="noopener">{ic("wa")}WhatsApp</a></div></div></div></section>'
def revcards(n=3): return ''.join(f'<figure class="rvw rv"><div class="stars" aria-label="Bintang 5">{ic("star")*5}</div><blockquote>“{q}”</blockquote><figcaption>Ulasan Google Maps</figcaption></figure>' for q in REV[:n])
def subj(): return ''.join(f'<div class="sj rv"><span class="sji">{ic(i)}</span><h3>{n}</h3></div>' for n, i in SUBJ)
def pcard(p, k):
    mt = ''.join(f'<li>{ic("check")}{m}</li>' for m in p['mat'])
    return f'''<article class="pcard p{k} rv"><figure class="imgr">{img(p['img'], p['n']+' – dokumentasi belajar')}</figure><div class="pc-b"><p class="lv">{p['lv']}</p><h3>{p['n']}</h3><p>{p['d']}</p><ul class="chk">{mt}</ul>
<div class="acts"><a class="btn btn-r" href="{{R}}program/{p['slug']}/index.html">Lihat detail</a><a class="btn btn-o" href="{wam('program '+p['n'])}" target="_blank" rel="noopener">{ic('wa')}Konsultasi</a></div></div></article>'''

def build():
    write_soc()
    # BERANDA
    home = f'''<section class="hero"><div class="wrap hero-g"><div class="hero-t"><p class="chip rv">{B['tag']}</p><h1 class="rv">Belajar Lebih Menyenangkan, Tumbuh Lebih Percaya Diri!</h1>
<p class="lede rv">Bimbel AKSI mendampingi anak belajar membaca, menulis, berhitung, dan memahami pelajaran sekolah melalui suasana belajar yang menyenangkan.</p>
<div class="acts rv"><a class="btn btn-r btn-l" href="{{R}}pendaftaran/index.html">Konsultasi Sekarang</a><a class="btn btn-o btn-l" href="{{R}}program/index.html">Lihat Program Belajar</a></div><p class="mini-rate rv">{stars()}</p></div>
<div class="hero-v"><span class="blob b1"></span><span class="blob b2"></span><figure class="arch">{img('papan-tulis','Anak berlatih berhitung di papan tulis',lazy=False,w=1080,h=802)}</figure><div class="tag"><strong>Calistung & SD kelas 1–5</strong><span>Ganting, Gedangan, Sidoarjo</span></div></div></div></section>
<section class="sec"><div class="wrap two"><div><h2 class="rv">Tempat belajar yang dekat, hangat, dan terarah.</h2></div><div><p class="rv">Bimbel AKSI adalah pusat bimbingan belajar di Ganting, Gedangan, Sidoarjo. Kami mendampingi anak belajar Calistung dan pelajaran SD, termasuk pengerjaan PR dan evaluasi perkembangan belajar.</p><a class="more rv" href="{{R}}tentang/index.html">Kenali Bimbel AKSI {ic('arrow')}</a></div></div></section>
<section class="sec soft"><div class="wrap"><h2 class="rv">Program unggulan</h2><div class="g2">{pcard(PR[0],0)}{pcard(PR[1],1)}</div><p class="note rv">{NOTE}</p></div></section>
<section class="sec"><div class="wrap"><h2 class="rv">Mengapa memilih Bimbel AKSI</h2><div class="bento">
<div class="bx bx-r rv"><h3>Suasana yang menyenangkan</h3><p>Anak belajar di ruang yang nyaman dengan pendamping yang sabar, sebagaimana tertulis di ulasan Google Maps.</p></div>
<div class="bx bx-y rv"><h3>Sesuai kurikulum sekolah</h3><p>Pembelajaran SD mengikuti kurikulum sekolah.</p></div>
<div class="bx bx-g rv"><h3>Bantu kerjakan PR</h3><p>Bimbingan pengerjaan PR agar anak tidak belajar sendirian.</p></div>
<div class="bx bx-n rv"><h3>Terpantau</h3><p>Evaluasi dan pelaporan perkembangan belajar.</p></div></div></div></section>
<section class="band"><img src="{{R}}assets/img/kelas-3.webp" alt="Ruang belajar dengan dinding berwarna" loading="lazy" width="1080" height="794"><div class="wrap band-t"><h2 class="rv">Dokumentasi belajar yang asli, bukan foto stok.</h2><a class="btn btn-y btn-l" href="{{R}}galeri/index.html">Lihat galeri</a></div></section>
<section class="sec"><div class="wrap"><h2 class="rv">Mata pelajaran bimbingan SD</h2><div class="g4">{subj()}</div><p class="note rv">Ketersediaan mata pelajaran per hari tidak dijamin; tanyakan jadwal terbaru.</p></div></section>
<section class="sec soft"><div class="wrap two"><div><h2 class="rv">Modul dan materi pembelajaran</h2><p class="rv">Anak belajar dengan buku modul seperti seri Saya Pandai Baca dan Saya Pintar Berhitung. Edisi dan ketersediaan terbaru dikonfirmasi melalui WhatsApp.</p><div class="acts"><a class="btn btn-r" href="{{R}}modul/index.html">Lihat modul</a></div></div><figure class="imgr plain rv">{img('modul','Buku modul Calistung Bimbel AKSI',w=529,h=661)}</figure></div></section>
<section class="sec"><div class="wrap"><h2 class="rv">Aktivitas dan kegiatan siswa</h2><div class="mini">{''.join(f'<figure class="m{i} imgr rv">{img(f,a,w=1080,h=1080)}</figure>' for i,(f,a) in enumerate([('luar-pohon','Kegiatan belajar di luar kelas'),('aktivitas-1','Aktivitas anak duduk bersama di luar ruangan'),('bersama','Dokumentasi bersama siswa'),('meja-anak','Anak-anak mengerjakan tugas di meja')]))}</div>
<h3 class="rv sp">Pendampingan dan evaluasi</h3><ul class="pills rv">{''.join(f'<li>{ic(i)}{n}</li>' for n,i in SUPPORT)}</ul><p class="note rv">Aktivitas tercantum di materi promosi. Detail ketersediaan dan jadwal dikonfirmasi lewat WhatsApp.</p></div></section>
<section class="sec soft"><div class="wrap"><div class="shead"><h2 class="rv">Kata orang tua di Google Maps</h2><a class="more" href="{{R}}testimoni/index.html">Semua ulasan {ic('arrow')}</a></div><div class="g3">{revcards()}</div></div></section>
<section class="sec"><div class="wrap two"><div><h2 class="rv">Lokasi dan kontak</h2><p class="addr rv">{ic('pin')}<span>{B['addr']}</span></p><div class="acts"><a class="btn btn-r" href="{wa()}" target="_blank" rel="noopener">{ic('wa')}{B['wad']}</a><a class="btn btn-o" href="{B['map']}" target="_blank" rel="noopener">Buka Google Maps</a></div></div><div class="map rv"><iframe title="Peta lokasi Bimbel AKSI" src="{embed()}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>{cta()}'''
    write('', page('Bimbel AKSI Gedangan Sidoarjo | Calistung dan Bimbingan Belajar SD', 'Bimbel AKSI di Gedangan, Sidoarjo menyediakan program Calistung dan bimbingan belajar SD. Hubungi kami untuk informasi program dan konsultasi belajar anak.', home, 0, 'home'))
    # TENTANG
    tent = f'''{phead('Tentang Bimbel AKSI','Pusat bimbingan belajar di Ganting, Gedangan, Sidoarjo untuk anak usia dini hingga SD.')}
<section class="sec"><div class="wrap two"><figure class="arch rv">{img('bersama','Dokumentasi bersama siswa Bimbel AKSI',w=1077,h=1400)}</figure><div><h2 class="rv">Mendampingi anak belajar dengan sabar</h2><p class="rv">Bimbel AKSI menyediakan bimbingan Calistung dan bimbingan belajar SD. Berdasarkan ulasan orang tua di Google Maps, anak merasa nyaman dan pengajarnya sabar dalam membimbing.</p><p class="rv">Selain pelajaran, ada pendampingan pengerjaan PR serta evaluasi dan pelaporan perkembangan belajar.</p></div></div></section>
<section class="sec soft"><div class="wrap"><h2 class="rv">Yang kami dampingi</h2><div class="g3"><div class="mx rv"><h3>Calistung</h3><p>Membaca, menulis, dan berhitung dengan buku modul.</p></div><div class="mx rv"><h3>Pelajaran SD</h3><p>Bahasa Indonesia, Bahasa Inggris, Matematika, dan IPAS.</p></div><div class="mx rv"><h3>Pengerjaan PR</h3><p>Anak dibimbing mengerjakan PR dari sekolah.</p></div></div></div></section>
<section class="sec"><div class="wrap"><h2 class="rv">Suasana belajar</h2><div class="mini">{''.join(f'<figure class="m{i} imgr rv">{img(f,a)}</figure>' for i,(f,a) in enumerate([('kelompok-1','Pembelajaran kelompok dengan modul'),('dinding','Dinding ruang belajar bergambar pelangi dan logo AKSI'),('kelas-1','Suasana kelas bersama'),('belajar-1','Anak-anak belajar di meja lipat')]))}</div></div></section>{cta()}'''
    write('tentang', page('Tentang Bimbel AKSI | Bimbingan Belajar Gedangan Sidoarjo', 'Profil Bimbel AKSI: pendampingan Calistung dan bimbingan belajar SD di Ganting, Gedangan, Sidoarjo.', tent, 1, 'tentang', 'bersama'))
    # PROGRAM
    write('program', page('Program Belajar Bimbel AKSI | Calistung & Bimbingan SD', 'Program Calistung dan bimbingan belajar SD kelas 1–5 di Bimbel AKSI Gedangan, Sidoarjo.', f'''{phead('Program belajar','Dua program utama, ditambah pendampingan dan evaluasi.')}<section class="sec"><div class="wrap"><div class="g2">{pcard(PR[0],0)}{pcard(PR[1],1)}</div><p class="note rv">{NOTE}</p></div></section>
<section class="sec soft"><div class="wrap"><h2 class="rv">Pendampingan dan evaluasi</h2><ul class="pills rv">{''.join(f'<li>{ic(i)}{n}</li>' for n,i in SUPPORT)}</ul><p class="note">Aktivitas pendukung dari materi promosi. Ketersediaan dan jadwal dikonfirmasi lewat WhatsApp.</p></div></section>
<section class="sec"><div class="wrap"><div class="info rv"><h3>Siswa kelas 6 SD</h3><p>Kelas 6 memiliki perlakuan khusus. Silakan konsultasikan kebutuhan anak Anda.</p><a class="btn btn-r" href="{{R}}pendaftaran/index.html?program=Konsultasi%20Kelas%206%20SD">Konsultasi Kelas 6</a></div></div></section>{cta()}''', 1, 'program'))
    # DETAIL
    for k, p in enumerate(PR):
        mt = ''.join(f'<li class="rv">{ic("check")}{m}</li>' for m in p['mat']); ad = ''.join(f'<li class="rv">{ic("check")}{m}</li>' for m in p['adv'])
        if p['slug'] == 'calistung':
            mid = f'''<section class="sec soft"><div class="wrap"><h2 class="rv">Tiga kemampuan dasar</h2><ol class="steps">{''.join(f'<li class="st rv"><span class="sn">{ic(i)}</span><h3>{n}</h3><p>{d}</p></li>' for n,i,d in [('Membaca','abc','Mengenal huruf dan merangkai bacaan.'),('Menulis','pen','Melatih menulis dengan bimbingan.'),('Berhitung','calc','Mengenal angka dan operasi dasar.')])}</ol><p class="note">Tidak ada jaminan anak bisa membaca dalam waktu tertentu; setiap anak berkembang berbeda.</p></div></section>
<section class="sec"><div class="wrap two"><figure class="imgr plain rv">{img('modul','Buku modul Calistung',w=529,h=661)}</figure><div><h2 class="rv">Belajar dengan buku modul</h2><p class="rv">Modul Calistung menjadi materi pendukung belajar. Edisi dan ketersediaan terbaru dapat ditanyakan lewat WhatsApp.</p><a class="more rv" href="{{R}}modul/index.html">Lihat modul {ic('arrow')}</a></div></div></section>
<section class="sec soft"><div class="wrap"><h2 class="rv">Dokumentasi proses belajar</h2><div class="mini">{''.join(f'<figure class="m{i} imgr rv">{img(f,a)}</figure>' for i,(f,a) in enumerate([('papan-tulis','Anak berlatih berhitung di papan tulis'),('calistung-1','Anak mengerjakan kegiatan belajar'),('kelompok-1','Pembelajaran kelompok dengan modul'),('belajar-1','Anak-anak belajar di meja lipat')]))}</div></div></section>'''
        else:
            mid = f'''<section class="sec soft"><div class="wrap"><h2 class="rv">Mata pelajaran</h2><div class="g4">{subj()}</div><p class="note">Ketersediaan mata pelajaran per hari tidak dijamin; tanyakan jadwal terbaru.</p></div></section>
<section class="sec"><div class="wrap"><h2 class="rv">Dokumentasi belajar</h2><div class="mini">{''.join(f'<figure class="m{i} imgr rv">{img(f,a)}</figure>' for i,(f,a) in enumerate([('kelas-1','Suasana kelas bersama'),('kelas-2','Kelas dengan meja lipat dan karpet'),('kelompok-2','Anak belajar bersama pendamping'),('meja-anak','Anak-anak mengerjakan tugas di meja')]))}</div><div class="info rv"><h3>Kelas 6 SD</h3><p>Memiliki perlakuan khusus. Konsultasikan lebih lanjut.</p></div></div></section>'''
        det = f'''<section class="phead dk"><div class="wrap two"><div><p class="chip">{p['lv']}</p><h1 class="rv">{p['n']}</h1><p class="lede rv">{p['d']}</p><div class="acts"><a class="btn btn-y btn-l" href="{wam('program '+p['n'])}" target="_blank" rel="noopener">{ic('wa')}Konsultasi via WhatsApp</a></div></div><figure class="arch rv">{img(p['img'],p['n'],lazy=False)}</figure></div></section>
<section class="sec"><div class="wrap two"><div><h2 class="rv">Sasaran siswa</h2><p class="rv">{p['tgt']}</p><h2 class="rv sp">Materi pembelajaran</h2><ul class="chk">{mt}</ul></div><div><h2 class="rv">Keunggulan</h2><ul class="chk">{ad}</ul></div></div><div class="wrap"><p class="note">{NOTE}</p></div></section>{mid}
<section class="sec"><div class="wrap narrow"><h2 class="rv">Pertanyaan umum</h2>{''.join(f'<details class="rv"><summary>{q}{ic("plus")}</summary><p>{a}</p></details>' for q,a in FAQ)}</div></section>{cta()}'''
        write('program/' + p['slug'], page(f"{p['n']} | Bimbel AKSI Gedangan Sidoarjo", f"{p['n']} di Bimbel AKSI, Gedangan, Sidoarjo. {p['d']}", det, 2, 'program', p['img']))
    # GALERI
    flt = ''.join(f'<button class="fb-btn" data-f="{k}" aria-pressed="{"true" if k=="semua" else "false"}">{t}</button>' for k, t in CATS)
    gl = ''.join(f'<figure class="gi {k} imgr" data-c="{c}"><button class="gb" data-full="{{R}}assets/img/{f}.webp" data-alt="{a}" aria-label="Perbesar foto: {a}">{img(f,a)}</button></figure>' for f, a, c, k in GAL)
    write('galeri', page('Galeri Kegiatan Belajar | Bimbel AKSI Gedangan', 'Dokumentasi asli kegiatan belajar, Calistung, dan aktivitas siswa Bimbel AKSI.', f'''{phead('Kegiatan dan galeri','Dokumentasi asli kegiatan belajar di Bimbel AKSI.')}<section class="sec"><div class="wrap"><div class="filters" role="group" aria-label="Filter kategori">{flt}</div><div class="masonry" id="gal">{gl}</div></div></section>{cta()}<dialog id="lb" aria-label="Pratinjau foto"><button class="lb-x" aria-label="Tutup">{ic('x')}</button><img alt=""><p></p></dialog>''', 1, 'galeri'))
    # MODUL
    mc = ''.join(f'<article class="md rv"><h3>{n}</h3><p>{d}</p><a class="more" href="{wam(n.lower())}" target="_blank" rel="noopener">Tanyakan Modul {ic("arrow")}</a></article>' for n, d in MODUL)
    write('modul', page('Modul dan Materi Belajar | Bimbel AKSI', 'Buku modul membaca, berhitung, Calistung, Matematika, dan Bahasa Inggris dari Bimbel AKSI.', f'''{phead('Modul dan materi belajar','Buku modul pendukung untuk anak belajar membaca, berhitung, dan pelajaran SD.')}<section class="sec"><div class="wrap two"><figure class="imgr plain rv">{img('modul','Buku modul Calistung Bimbel AKSI',w=529,h=661)}</figure><div class="g1">{mc[:0]}<div class="mdg">{mc}</div></div></div></section>
<section class="sec soft"><div class="wrap two"><div><h2 class="rv">Merchandise Bimbel AKSI</h2><p class="rv">Kaos bertema AKSI tersedia sebagai merchandise. Tanyakan ukuran dan ketersediaan melalui WhatsApp.</p><a class="btn btn-r" href="{wam('merchandise Bimbel AKSI')}" target="_blank" rel="noopener">{ic('wa')}Tanyakan Merchandise</a></div><figure class="imgr plain rv">{img('kaos','Kaos Bimbel AKSI',w=496,h=271)}</figure></div><div class="wrap"><p class="note">Gambar berasal dari materi promosi lama. Harga dan edisi terbaru tidak ditampilkan; tanyakan lewat WhatsApp. Belum ada checkout online.</p></div></section>{cta()}''', 1, 'modul', 'modul'))
    # TESTIMONI
    write('testimoni', page('Testimoni Orang Tua | Bimbel AKSI Gedangan', 'Rating 5,0 dari 50 ulasan Google Maps untuk Bimbel AKSI Gedangan, Sidoarjo.', f'''{phead('Testimoni orang tua','Cuplikan ulasan asli dari Google Maps.')}<section class="sec"><div class="wrap"><div class="ratebig rv">{ring()}<div><h2>{B['rating']} / 5,0</h2><p>Dari {B['rev']} ulasan Google Maps</p><a class="more" href="{B['map']}" target="_blank" rel="noopener">Lihat di Google Maps {ic('arrow')}</a></div></div><div class="g3">{revcards()}</div><p class="note">Cuplikan ulasan ditampilkan apa adanya tanpa nama pengulas.</p></div></section>{cta()}''', 1, 'testimoni'))
    # PENDAFTARAN
    po = ''.join(f'<option>{x}</option>' for x in ['Calistung', 'Bimbingan Belajar SD', 'Konsultasi Kelas 6 SD'])
    write('pendaftaran', page('Konsultasi Program | Bimbel AKSI', 'Kirim permintaan konsultasi ke Bimbel AKSI melalui WhatsApp.', f'''{phead('Konsultasi calon siswa','Isi data singkat, lalu lanjutkan lewat WhatsApp.')}<section class="sec"><div class="wrap narrow"><form id="f" novalidate data-wa="{B['wa']}">
<div class="fld"><label for="ortu">Nama orang tua</label><input id="ortu" required autocomplete="name"><p class="err" role="alert"></p></div>
<div class="fld"><label for="siswa">Nama calon siswa (opsional)</label><input id="siswa"></div>
<div class="fld"><label for="wa">Nomor WhatsApp</label><input id="wa" inputmode="tel" required autocomplete="tel" placeholder="08xx-xxxx-xxxx"><p class="err" role="alert"></p></div>
<div class="row"><div class="fld"><label for="usia">Usia anak</label><input id="usia" inputmode="numeric" required placeholder="Contoh: 5"><p class="err" role="alert"></p></div><div class="fld"><label for="kelas">Jenjang / kelas</label><input id="kelas" required placeholder="Contoh: TK B atau SD kelas 2"><p class="err" role="alert"></p></div></div>
<div class="fld"><label for="program">Program yang diminati</label><select id="program" required><option value="">Pilih</option>{po}</select><p class="err" role="alert"></p></div>
<div class="fld"><label for="pesan">Pesan tambahan (opsional)</label><textarea id="pesan" rows="4"></textarea></div>
<button class="btn btn-r btn-l" type="submit">{ic('wa')}Lanjut ke WhatsApp</button><p class="note">Mengirim pesan lewat WhatsApp belum berarti siswa terdaftar secara resmi. Data tidak disimpan di server.</p></form></div></section>''', 1, 'pendaftaran'))
    # KONTAK
    write('kontak', page('Kontak dan Lokasi | Bimbel AKSI Gedangan Sidoarjo', 'Alamat, WhatsApp, email, Instagram, TikTok, dan Google Maps Bimbel AKSI di Ganting, Gedangan, Sidoarjo.', f'''{phead('Kontak dan lokasi','Hubungi kami untuk informasi program, jadwal, dan biaya terbaru.')}<section class="sec"><div class="wrap two"><div class="ctl"><h2 class="rv">{B['full']}</h2><p class="addr rv">{ic('pin')}<span>{B['addr']}</span></p>
<ul class="clist rv"><li>{soc('wa', wa(), 48)}<span>WhatsApp<br><a href="{wa()}" target="_blank" rel="noopener">{B['wad']}</a></span></li><li>{soc('mail','mailto:'+B['mail'],48,False)}<span>Email<br><a href="mailto:{B['mail']}">{B['mail']}</a></span></li><li>{soc('ig',B['ig'],48)}<span>Instagram<br><a href="{B['ig']}" target="_blank" rel="noopener">{B['igh']}</a></span></li><li>{soc('tt',B['tt'],48)}<span>TikTok<br><a href="{B['tt']}" target="_blank" rel="noopener">{B['tth']}</a></span></li></ul>
<div class="acts"><a class="btn btn-r" href="{wa()}" target="_blank" rel="noopener">{ic('wa')}Hubungi WhatsApp</a><a class="btn btn-o" href="{B['map']}" target="_blank" rel="noopener">Buka Google Maps</a><a class="btn btn-o" href="{B['ig']}" target="_blank" rel="noopener">Kunjungi Instagram</a><a class="btn btn-o" href="{B['tt']}" target="_blank" rel="noopener">Kunjungi TikTok</a></div><p class="note">Jam operasional belum diverifikasi, jadi tidak ditampilkan. Tanyakan lewat WhatsApp.</p></div>
<div class="map rv"><iframe title="Peta lokasi Bimbel AKSI" src="{embed()}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>{cta()}''', 1, 'kontak'))
    open(OUT + '/404.html', 'w').write(page('Halaman tidak ditemukan | Bimbel AKSI', 'Halaman tidak ditemukan.', '<section class="phead"><div class="wrap"><h1>Halaman tidak ditemukan</h1><p class="lede"><a class="btn btn-r" href="/index.html">Kembali ke beranda</a></p></div></section>', 0))
build(); print('ok')
