import sys
import re



#x should be the result of a regular exprestion




comands={
    'focusMode?': "81 09 04 38 FF",
    'focusPos?' : "81 09 04 48 FF"


};#string to hex
functionComands={
    'focus (.)(.)(.)(.)' : ("81 01 04 48 0p 0q 0r 0s FF",['p','q','r','s'])
}

responses={
    '90 50 0? 0? 0? 0? ff':'matchMore',
    '90 4. ff':"ACK",
    '90 5. ff':"Complete",
    '90 50 03 ff': "Manual Focus",
    '90 50 02 ff': "Auto Focus",
    '90 60 02 ff': ""


}

def translateResponse(resp):
    #? is wild card
    pre = "^"
    post = ""
    for s in list(responses.keys()):
        regExp=s.replace('?',"(.)")
        regExp=pre+regExp+post

        reg=re.compile(regExp)


        x=re.match(reg,resp)

        if x!=None:
            if responses[s]!="matchMore":

                return responses[s]
            else:
                temp=' '.join(x.groups())
                return temp
    return ""


def doSubstitution(tup,x):
    baseStr=tup[0]
    subOuts=tup[1]
    nums=x.groups();
    index=0
    for s in nums:
        baseStr=baseStr.replace(subOuts[index],s)
        index+=1
    return baseStr;


def specialComands(st):
    for regExp in list(functionComands.keys()):
        x=re.match(regExp,st)
        if x!=None:
            return doSubstitution(functionComands[regExp],x)

    return False




def stringToBytes(st):
    original=st
    temp=specialComands(st)
    if temp!=False:
        st=temp
    if st in comands.keys():
        st=comands[st]

    st = st.replace(" ", "")
    try:
        s = int(st.replace(" ", ""), 16)
    except ValueError:
        return original, True
    # print(len(st))
    # print(len(st)/2)
    return s.to_bytes(int(len(st) / 2), "big"), False

def getInput():

    st=input("Input hexadecimal value: ")

    #st="81 01 04 3f 02 00 ff"
    return stringToBytes(st)
