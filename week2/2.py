class Solution:
    def interpret(self, command: str) -> str:
        s=''
        for i in range(len(command)):
            if command[i]=='(' and command[i+1]==')':
                s+='o'
                i+=1
                
            elif command[i]=='(' or command[i]==')':
                s+=''
                
            else:
                s+=command[i]
                
        return s
