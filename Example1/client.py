# pip install requests

import requests


class NewRequest():
    def __init__(self, *, url: str):
        self.__url = url

    def getConnection(self, *, url) -> bool:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return True
            else:
                print(f'Ошибка соединения: {response.status_code}')
                return False
        except requests.Timeout:
            print('Сервер не отвечает. Попробуйте позднее.')
            return False
        except requests.ConnectionError:
            print('Ошибка соединения. Проверьте подключение к Интернету.')
            return False

    def getJson(self):
        connection = self.getConnection(url=self.__url)
        if connection:
            request = requests.get(self.__url)
            message = request.json()
            print(message)

    def getUser(self, *, id: str = 1):
        newUrl = f"{self.__url}/users/{id}"
        connection = self.getConnection(url=newUrl)
        if connection:
            request = requests.get(newUrl)
            message = request.json()
            print(message)

    def getAllUsers(self):
        newUrl = f"{self.__url}/usersall"
        connection = self.getConnection(url=newUrl)
        if connection:
            request = requests.get(newUrl)
            dataUsers = request.json()
            for user in dataUsers:
                print(user['name'])

    def addNewUser(self, *, userName: str):
        newUrl = f"{self.__url}/useradd/{userName}"
        try:
            request = requests.post(newUrl)
            message = request.json()
            print(message["data"])

        except Exception as error:
            print("Ошибка добавления: ", error)

    def changeNameUser(self, *, user_name: str, newName: str):
        newUrl = f"{self.__url}/user/changename?user_name={user_name}&new_name={newName}"
        try:
            request = requests.post(newUrl)
            message = request.json()
            print(message["data"])

        except Exception as error:
            print("Ошибка смены имени: ", error)


request1 = NewRequest(url="http://127.0.0.1:8000")
request1.getJson()

request2 = NewRequest(url="http://127.0.0.1:8000")
request2.getUser(id=2)

request3 = NewRequest(url="http://127.0.0.1:8000")
request3.getAllUsers()

request4 = NewRequest(url="http://127.0.0.1:8000")
request4.addNewUser(userName="Алеша")
request4.getAllUsers()

request5 = NewRequest(url="http://127.0.0.1:8000")
request5.changeNameUser(user_name="Ivan", newName="Абоба")