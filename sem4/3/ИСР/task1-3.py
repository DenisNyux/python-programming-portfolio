class Post():


    def __init__(self,nick='Nick',text='Hello world!'): 
        self.__verify_text(nick) # Проверяем ник
        self.__verify_text(text) # Проверяем текст поста
        self.__user_nick = nick  
        self.__user_text = text  
    

    @property
    def nickname(self):
        return self.__user_nick # getter
  
   
    @nickname.setter
    def nickname(self, nick): #setter
        try:
            self.__verify_text(nick)
        except ValueError as e:
            print(e)
        else:
            self.__user_nick = nick 


    @property
    def textPost(self):
        return self.__user_text


    @textPost.setter
    def textPost(self, text):
        try:
            self.__verify_text(text)
        except ValueError as e:
            print(e)
        else:
            self.__user_text = text 


    def __verify_text(self, text,field='text'):
        if len(text) == 0:
            raise ValueError(f'Поле {field} обязательное поле')

  
    def __str__(self): 
        return f"Author: {self.nickname} Text: {self.textPost}" 


# Наследуем Post
class Comment(Post): 
  
  
    def __init__(self,nick, text, rate=0): 
        Post.__init__(self, nick, text) 
        self.__rate = rate

    @property
    def comRate(self):
        return self.__rate
  
    @comRate.setter
    def comRate(self,rate):
        self.__rate = rate

    def addRate(self): #Метод класса, который увеличивает рейтинг
        self.__rate += 1
  
    def __str__(self): #Вывод содержания экземпляра
        return f"Author: {self.nickname} Text: {self.textPost} Rating: {self.__rate}" 

post_instance = Post('DenisNyux','Hello world. How are you?')
print(post_instance.nickname, post_instance.textPost, '\n', post_instance)

comment_instance = Comment('Nick', 'Hi, Den!')
comment_instance.addRate()
print(comment_instance)
