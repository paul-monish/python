class Demo:
    def Get_String(self,str):
        self.str=str
       
        
    def Print_String(self):
        print(self.str.upper())
        
st=Demo()
s=input("Enter String in Lower Case:")
st.Get_String(s)
st.Print_String()
    
        