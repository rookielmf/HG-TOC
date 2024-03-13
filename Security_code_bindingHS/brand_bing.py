'''
@create : lisa
@file :security_code
@Date :2024/3/6
@desc :
'''
from Security_code_bindingHS.get_security_code import bind_security_code


def main():
    #品牌站枚举
    brands = ['elfbar','lostmary','ELFLIQ','FunkyRepublic','EBDesign','EBCREATE','FUNKY_LANDS','HIDESEEK','RabBeatsVape','LOSTY_LOSTY','MAD_EYES','OFF_STAMP','URBAN_TALE','LOSGAL','MARYLIQ']
    #调用绑定防伪码方法之前清空OUT TXT
    with open(brands[1]+'_secuirty_code_out.txt','w'):
        pass
    #HS数据库防伪码ID枚举
    HS_security_id =[17641,17642,17643,17644,17645]
    #HS数据库防伪码ID数量
    num = len(HS_security_id)
    print(num)
    #调用绑定防伪码方法
    bind_security_code(brands[1],HS_security_id,num)

if __name__ == '__main__':
    main()
