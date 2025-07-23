const swiper = new Swiper('.mySwiper', {
    // общее
    loop: true,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    // ключевые точки
    breakpoints: {
        // до 768px — 1 слайд
        0: {
            slidesPerView: 1,
            spaceBetween: 16,
        },
        // от 769px до 1024px — 2 слайда
        769: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        // от 1025px — 3 слайда
        1025: {
            slidesPerView: 3,
            spaceBetween: 24,
        },
    }
});

const menuToggle = document.getElementById('menuToggle');
const headerNav = document.getElementById('headerNav');
menuToggle.onclick = function() {
    headerNav.classList.toggle('open');
    document.body.classList.toggle('menu-open');
};
// По клику на ссылку закрываем меню (опционально)
headerNav.querySelectorAll('a').forEach(link => {
    link.onclick = () => {
        headerNav.classList.remove('open');
        document.body.classList.remove('menu-open');
    };
});
// Для раскрытия подменю Каталог по клику
document.querySelectorAll('.has-dropdown > a').forEach(link => {
    link.onclick = function(e) {
        if (window.innerWidth <= 900) {
            e.preventDefault();
            this.parentElement.classList.toggle('open');
        }
    }
});


document.querySelectorAll('.lightbox').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const imgSrc = this.getAttribute('href');
        const lightbox = document.getElementById('lightboxModal');
        const lightboxImg = document.getElementById('lightboxImg');
        lightboxImg.src = imgSrc;
        lightbox.classList.add('active');
    });
});

function closeLightbox() {
    document.getElementById('lightboxModal').classList.remove('active');
    document.getElementById('lightboxImg').src = '';
}
document.addEventListener("DOMContentLoaded", function() {
    const swiperEl = document.querySelector('.mySwiper');
    if (swiperEl) {
        new Swiper(".mySwiper", {
            loop: true,
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            slidesPerView: 3,
            spaceBetween: 30,
            breakpoints: {
                0: { slidesPerView: 1 },
                768: { slidesPerView: 2 },
                1024: { slidesPerView: 3 }
            }
        });
    }
});