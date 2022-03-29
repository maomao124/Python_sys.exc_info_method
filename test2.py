"""
 * Project name(项目名称)：Python_sys.exc_info方法
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 10:56
 * Version(版本): 1.0
 * Description(描述)： 
 """

import sys
import traceback

if __name__ == '__main__':
    try:
        a = 2 / 0
    except:
        print("异常类型：", sys.exc_info()[0])
        print("异常内容：", sys.exc_info()[1])
        traceback.print_tb(sys.exc_info()[2])
