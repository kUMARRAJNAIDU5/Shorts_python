import inspect
from dataclasses import asdict, astuple
from dataclasses import dataclass
from pprint import pprint


@dataclass
class Comment:
    id:int
    text:str

    def add_comments(self)->str:
        pass

    def remove_comments(self) -> str:
        pass

def main():
    comment=Comment(1,"Going on world tour")
    lst_com=[]
    for idx in range(5):
        c=Comment(idx, "kumar:"+str(idx))
        lst_com.append(c)

    print(comment)
    print(astuple(comment))
    print(asdict(comment))
    print('******************************************')
    pprint(inspect.getmembers(Comment,inspect.isfunction))
    print('******************************************')
    print(lst_com)

if __name__ == '__main__':
    main()