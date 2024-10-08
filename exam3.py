class Article : 
    def __init__(self) :
        self.num = 0
        self.title = None
        
class FileArticle(Article) :
    def __init__(self) :
        self.fileName = None
        
    # java의 toString()과 기능이 같은 함수
    def __str__(self) :
        return '자료실 [번호={}, 제목={}, 첨부파일={}]'\
                .format(self.num, self.title, self.fileName)

class QNAArticle(Article) :
    def __init__(self) :
        self.answer = None
        
    def __str__(self) :
        return '질문/답변 [번호={}, 제목={}, 답변={}]'\
                .format(self.num, self.title, self.answer)
    
file = FileArticle()
file.num = 1
file.title = '첫번째 자료입니다.'    
file.fileName = 'python.txt'
#print(file.__str__())
print(file)
print('-' * 20)

qna = QNAArticle()
qna.num = 1
qna.title = '첫번째 질문입니다.'
qna.answer = '첫번째 답변입니다.'
print(qna)
    
