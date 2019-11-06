import cmd
class SuperOutil(cmd.Cmd):
    """
        Docstring de ma classe SuperOutil
        Lance un super outil !
    """
    intro = "Entrez une commande suivie d'entiers.\n"
    prompt = '(superoutil) '
    def do_max(self, arg):
        "Calculer le max d'une liste d'entiers"
        liste = map(int, arg.split())
        print(max(liste))
    def do_sum(self, arg):
        "Calculer la somme d'une liste d'entiers"
        liste = map(int, arg.split())
        print(sum(liste))

SuperOutil().cmdloop()
