M = 'manga'
TITLE_TYPE_CHOICES = [
    (M, 'Манга'),
    ('manhwa', 'Манхва'),
    ('manhua', 'Маньхуа'),
    ('rumanga', 'Руманга'),
    ('OEL-manga', 'OEL-манга'),
    ('comic', 'Западный комикс')
]
RELEASE_FORMAT_CHOICES = (
        ('4-koma', '4-кома (Ёнкома)'),
        ('in color', 'В цвете'),
        ('web', 'Веб'),
        ('webtoon', 'Вебтун'),
        ('doujinshi', 'Додзинси'),
        ('manga collection', 'Сборник'),
        ('single', 'Сингл')
)
TITLE_STATUS_CHOICES = (
        ('ongoing', 'Онгоинг'),
        ('finish', 'Завершён'),
        ('anons', 'Анонс'),
        ('stopped', 'Приостановлен'),
        ('discontinued', 'Выпуск прекращён'),
)
TRANSLATOR_STATUS_CHOICES = (
    ('continued', 'Продолжается'),
    ('finished', 'Завершён'),
    ('frozen', 'Замарожен'),
    ('abandoned', 'Заброшен'),
)
ADULT_CONTENT_CHOICES = (
    ('no', 'Нет'),
    ('yes 16+', 'Да 16+'),
    ('Yes 18+', 'Да 18+'),
)
DOWNLOAD_CHAPTER_CHOICES = (
    ('All', 'Все'),
    ('Only', 'Создатель и Переводчики')
)
