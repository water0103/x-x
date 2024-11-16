#https://www.google.com/search?q=projection+matrix+in+pygame&sca_esv=7d18109a394306ad&sxsrf=ADLYWIIiIuGb3NFXLvwPi9MuFd8_PB94hQ%3A1728723359344&ei=nzkKZ97aFOW5vr0PiLHw2Q0&ved=0ahUKEwiepv6tvIiJAxXlnK8BHYgYPNsQ4dUDCA8&uact=5&oq=projection+matrix+in+pygame&gs_lp=Egxnd3Mtd2l6LXNlcnAiG3Byb2plY3Rpb24gbWF0cml4IGluIHB5Z2FtZTIFECEYoAEyBRAhGKABSO4iUK8DWO0gcAN4AZABAJgBTaABuQKqAQE2uAEDyAEA-AEBmAIJoALFAsICChAAGLADGNYEGEfCAgYQABgNGB7CAgQQABgewgIGEAAYCBgewgIIEAAYCBgNGB7CAggQABiABBiiBMICBxAhGKABGAqYAwCIBgGQBgKSBwE5oAf0Dw&sclient=gws-wiz-serp#fpstate=ive&vld=cid:dcf72589,vid:qw0oY6Ld-L0,st:0
import numpy as np
k = ([[1 , 1 , 1],
      [1 , 1 , 1],
      [1 , 1 , 1]])
projection_matrix = np.matrix([[1, 0, 0],
                               [0, 1, 0]],)
x = np.dot(projection_matrix , k)
print(x)