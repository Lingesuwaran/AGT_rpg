import pyfiglet 
from colorama import Fore, Back, Style  #Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
                                        #Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
                                        #Style: DIM, NORMAL, BRIGHT, RESET_ALL
import gpt_2_simple as gpt2

def Play(a):

  file_name = "/content/AGT_rpg/Books/data.txt"

  l=pyfiglet.figlet_format("Loading...", font = "slant")
  g=pyfiglet.figlet_format("Generating world...", font = "slant")
  print(Fore.GREEN)

  gpt2.download_gpt2(model_name="774M")
  print(Style.BRIGHT+g)
  sess = gpt2.start_tf_sess()

  gpt2.finetune(
      sess,
      dataset  = file_name,
      model_name = '774M',
      steps=1000,
      restore_from='fresh',
      run_name = 'run1',
      print_every = 1000,
      sample_every = 5000,
      save_every = 100         
                )

  print(Style.BRIGHT+l)
  print(Fore.RESET)
  input1=""
  while input1 != 'esc':
    input1 = input("Enter something or esc to exit")
    gpt2.generate(sess,
                length=250,
                temperature=0.7,
                prefix=input1,
                nsamples=5,
                batch_size=5,
                top_k=40,
                run_name='run1'
                )




if __name__ == "__main__":
  print(Fore.MAGENTA)
  #print(Back.BLACK)
  result1 = pyfiglet.figlet_format("AGT", font = "isometric1") 
  result2 = pyfiglet.figlet_format(" rpg", font = "slant")
  print(Style.BRIGHT+result1+result2) 
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
