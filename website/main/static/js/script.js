// Функция для отслеживания прокрутки страницы
window.addEventListener('scroll', function () {
    if (window.scrollY > 0) {
        document.body.classList.add('scrolling'); // Добавить класс при прокрутке
    } else {
        document.body.classList.remove('scrolling'); // Убрать класс, если прокрутка в верхней части
    }
});


