class Solution:
    def simplifyPath(self, path: str) -> str:

        ret = []
        stri = ''
        path+= '/'
        for s in path: 
            if s != '/':
                stri+= s

            if stri and s == '/':

                if stri == '..':
                    if ret: 
                        ret.pop()
                elif stri == '.':
                    pass
                else: 
                    ret.append (stri)
                stri = ''


        res = '/' + '/'.join (ret)

        return res



        

      