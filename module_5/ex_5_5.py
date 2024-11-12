import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def __str__(self):
        return f"Пользователь: {self.nickname}, пароль: {self.password}, возраст: {self.age}"


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Название: {self.title}, длительность: {self.duration}, текущее время: {self.time_now}, взрослый режим: {self.adult_mode}"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return True
        return False

    def register(self, nickname, password, age):
        if nickname in [user.nickname for user in self.users]:
            return f"Пользователь {nickname} уже существует"
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user
        return True

    def log_out(self):
        self.current_user = None

    def add(self, video):
        if video.title not in [video.title for video in self.videos]:
            self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, video_title):
        for video in self.videos:
            if video.title == video_title:
                print(f"Просмотр видео: {video.title}")
                print(f"Текущее время: {video.time_now}")
                time.sleep(1)
                video.time_now += 1
                if self.current_user is None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                    return
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                
                print(f"Текущее время: {video.time_now}")
                print("Конец видео")
                video.time_now = 0
                return
        print(f"Видео {video_title} не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1)
ur.add(v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')