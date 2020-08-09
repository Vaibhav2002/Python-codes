print("".join(chr(ord("z")-ord(i)+ord("a")) if i.islower() else chr(ord("Z")-ord(i)+ord("A")) for i in input()))
