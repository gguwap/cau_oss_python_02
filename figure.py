import math # math 모듈의 PI와 sqrt를 사용하기 위해 모듈 불러오기

class Line:
    def __init__(self, length = 1):
        self.__length = length

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length
    
    def area_square(line):
        #docstring의 작성방법은 다음과 같습니다.
        


        return line.get_length() ** 2
    
    def area_circle(line):

        return line.get_length() ** 2 * math.pi
    
    def area_regular_triangle(line):

        return line.get_length() ** 2 * math.sqrt(3) / 4
    