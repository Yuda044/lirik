import sys
import time

def jalanin_lirik():
    lirik = [
       ("How can we go back to being friends", 0.09),
       ("When we just shared a bed", 0.09),
       ("How can you look at me and pretend", 0.09),
       ("I'm someone you've never met?", 0.09),
       ("", 0.0), ("", 0.0), # baris kosong untuk jeda paragraf
       ("It was last December", 0.09),
       ("You were layin' on my chest", 0.09),
       ("I still remember", 0.09),
       ("I was scared to take a breath, didn't want you to move your head", 0.09),
       ("", 0.0), ("", 0.0), # baris kosong untuk jeda paragraf
       ("How can we go back to being friends", 0.09),
       ("When we just shared a bed? (Yeah)", 0.09),
       ("How can you look at me and preten", 0.09),
       ("I'm someone you've never met?", 0.09),
  
    ] 

    delay_baris = 2
    delay_paragraf = 0.09   # jeda khusus antar paragraf

    print("\n== back to friends ==")
    time.sleep(2)

    for baris_lagu, delay_karakter in lirik:
        for karakter in baris_lagu:
            print(karakter, end="")
            sys.stdout.flush()
            time.sleep(delay_karakter)

        print("")  # pindah baris

        # kalau baris kosong, kasih jeda lebih lama
        if baris_lagu == "":
            time.sleep(delay_paragraf)
        else:
            time.sleep(delay_baris)

    print("// Code by Masbay")

jalanin_lirik()
