import pyfiglet 
from colorama import Fore, Back, Style  #Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
                                        #Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
                                        #Style: DIM, NORMAL, BRIGHT, RESET_ALL
import gpt_2_simple as gpt2

world = "world"
def Play(a):
  sess = gpt2.start_tf_sess()
  gpt2.generate(sess,
              length=250,
              temperature=0.7,
              prefix="%Name%",
              nsamples=5,
              batch_size=5,
              top_k=40,
              run_name=world
              )




if __name__ == "__main__":
  print(Fore.MAGENTA + 'some red text')
  #print(Back.BLACK)
  result1 = pyfiglet.figlet_format("AGT", font = "isometric1") 
  result2 = pyfiglet.figlet_format(" rpg", font = "slant")
  print(Style.BRIGHT+result1+result2) 
  from colorama import Fore, Back, Style
  #Menu
  print("1. Play \n2. Load \n3.Exit")
  while True:
    inp=input(">>")

    if inp=="1":
      Play("1")
    elif inp=="2":
      print("Load")
    elif inp=="3":
      exit()
    else:
      print("Enter a valid option")
