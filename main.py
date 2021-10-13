def citire_lista():
    """
    Functia citeste o lista
    :return: lista
    """
    lista = []
    lungime_lista = int(input("Lungimea liste :"))
    nr_element = 1
    while lungime_lista:
        element = int(input(f"Elementul {nr_element} este :"))
        lista.append(element)
        lungime_lista = lungime_lista - 1
        nr_element = nr_element + 1
    return lista


def nr_prim(nr):
    """
    :param nr: numarul pe care il verificam daca este prim
    :return: true daca nr este prim si false in caz contrar
    """
    if nr < 2:
        return False
    for i in range(2, nr):
        if nr % i == 0:
            return False
    return True


def test_nr_prim():
    """
    Functie test pentru functia nr_prim
    """
    assert nr_prim(13) == True
    assert nr_prim(12) == False
    assert nr_prim(14) == False


def get_longest_all_primes(lista_principala):
    """
    Functie care determina cea mai lunga subsecventa in care toate numerele sunt prime
    :param lista_principala:
    :return:
    """
    lungime_max = 0
    lungime_actual = 0
    secv_max = []
    secv_act = []
    for n in lista_principala:
        if nr_prim(n):
            lungime_actual = lungime_actual + 1
            secv_act.append(n)
        else:
            if lungime_actual > lungime_max:
                lungime_max = lungime_actual
                secv_max = secv_act

            lungime_actual = 0
            secv_act = []

    if lungime_actual > lungime_max:
        secv_max = secv_act
    return secv_max


def test_get_longest_all_primes():
    """
    Functie de test pentru functia get_longest_all_primes
    :return:
    """
    assert (get_longest_all_primes([1, 5, 7, 12, 7, 3, 5, 19, 15, 2]) == [7, 3, 5, 19])
    assert (get_longest_all_primes([1, 5, 7, 12, 7, 3, 5, 19]) == [7, 3, 5, 19])
    assert (get_longest_all_primes([4, 6, 8, 10, 15, 49]) == [])
    assert (get_longest_all_primes([1, 2, 4, 5, 8, 7]) == [2])


def nr_divizori(nr):
    """
    :param nr: un numar int
    :return: cati divizori are nr
    """
    numar_divizori = 0
    if nr == 1:
        numar_divizori = 1
    else:
        for i in range(2, (nr // 2) + 1):
            if nr % i == 0:
                numar_divizori += 1

    return numar_divizori


def test_nr_divizori():
    assert nr_divizori(6) == 2
    assert nr_divizori(12) == 4


def get_longest_same_div_count(lista_principala):
    """
    Functie care determina cea mai lunga subsecventa in care toate numerele au acelasi numar de divizori
    :param lst:
    :return: O lista de intregi care reprezinta cea mai lunga subsecventa in care toate numerele au acelasi numar de divizori
    """
    
    lmax = 0
    secv_max = []
    lactual = 1
    nrdiv = nr_divizori(lista_principala[0])
    secv_actuala = [lista_principala[0]]
    
    for n in range (1,len(lista_principala)):
       if(nr_divizori(lista_principala[n]) == nrdiv):
            lactual = lactual + 1
            secv_actuala.append(lista_principala[n])
       else:
           if(lactual > lmax):
                lmax = lactual
                secv_max = secv_actuala
           secv_actuala = [lista_principala[n]]
           lactual = 1
           nrdiv = nr_divizori(lista_principala[n])
            
    if(lactual > lmax):
        secv_max = secv_actuala
    return secv_max


def test_get_longest_same_div_count():
    """
    Functia care testeaza functia get_longest_same_div_count
    :return:
    """
    assert (get_longest_same_div_count([6, 8, 10, 9, 25, 2]) == [6, 8, 10])
    assert (get_longest_same_div_count([7, 2, 9, 25]) == [7, 2])
    assert (get_longest_same_div_count([1, 2, 4]) == [1])
    assert (get_longest_same_div_count([6, 9, 25, 49, 10, 8, 2]) == [9, 25, 49])


def is_palindrome(n):
    """
    :param copie: retinem nr n
    :param invers: formam inversul numarului n
    :param n: numarul pe care il verificam daca este palindrom
    :return: true daca nr este palindrom sau false in caz contrar
    """
    copie = n
    invers = 0
    while copie > 0:
        invers = invers * 10 + copie % 10
        copie = copie // 10
    if n == invers:
        return True
    else:
        return False

def test_nr_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(232) == True


def get_longest_all_palindromes(lista_principala):
    """

    :param lista_principala:
    :return: cea mai lunga subsecventa de nr palindrome
    """
    lungime_max = 0
    lungime_actuala = 0
    secventa_max = []
    secventa_actuala = []
    for n in lista_principala:
        if is_palindrome(n):
            lungime_actuala +=  1
            secventa_actuala.append(n)
        else:
            if lungime_actuala > lungime_max:
                lungime_max = lungime_actuala
                secventa_max = secventa_actuala

            lungime_actuala = 0
            secventa_actuala = []

    if lungime_actuala > lungime_max:
        secventa_max = secventa_actuala

    return secventa_max

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([121, 232, 343]) == [121, 232, 343]
    assert get_longest_all_palindromes([21, 212, 121]) == [212 ,121]


def is_crescator(x):
    """
    
    :param x: un numar natural
    :return: true daca cifrele numarului x sunt in ordine crescatoare si fals in caz contrar
    """
    copie = x
    nr_cifre = 0
    var = 0
    while copie > 9:
        nr_cifre += 1
        copie //= 10
    copie = x

    for i in range(copie//10**nr_cifre , copie//10%10+1):
        for j in range(copie//10**(nr_cifre-1)%10, copie%10+1):
            if(i<j):
                var+=1
    if var >= nr_cifre:
        return True
    else:
        return False

def test_is_crescator():
    assert is_crescator(123) == True
    assert is_crescator(12343) == False
    assert is_crescator(321) ==False


def get_longest_digit_count_desc(lista_principala):
    """

       :param lista_principala:
       :return: cea mai lunga subsecventa de numere cu prop ca cifrele numerelor sunt in oridine crescatoare
       """
    lungime_max = 0
    lungime_actuala = 0
    secventa_max = []
    secventa_actuala = []
    for x in lista_principala:
        if is_crescator(x):
            lungime_actuala += 1
            secventa_actuala.append(x)
        else:
            if lungime_actuala > lungime_max:
                lungime_max = lungime_actuala
                secventa_max = secventa_actuala

            lungime_actuala = 0
            secventa_actuala = []

    if lungime_actuala > lungime_max:
        secventa_max = secventa_actuala

    return secventa_max


def main():
    test_nr_prim()
    test_get_longest_all_primes()
    test_nr_divizori()
    test_get_longest_same_div_count()
    test_nr_palindrome()
    test_get_longest_all_palindromes()
    test_is_crescator()

    lista_principala = []
    f = False
    while f != True:
        print("1. Citire data pentru lista")
        print("2. Det. cea mai lunga subsecventa cu proprietatea 1")
        print("3. Det. cea mai lunga subsecventa cu proprietatea 2")
        print("4. Det. cea mai lunga subsecventa cu proprietatea 3")
        print("5. Det. cea mai lunga subsecventa cu proprietatea 4")
        print("6. Iesire din program")
        print()
        optiune = int(input("Dati obtiunea:"))

        if optiune == 1:
            lista_principala = citire_lista()
            print()
        if optiune == 2:
            secv1 = get_longest_all_primes(lista_principala)
            print(secv1)
            print()
        if optiune == 3:
            secv2 = get_longest_same_div_count(lista_principala)
            print(secv2)
            print()
        if optiune == 4:
            secv3 = get_longest_all_palindromes(lista_principala)
            print(secv3)
            print()
        if optiune == 5 :
            secv4 = get_longest_digit_count_desc(lista_principala)
            print(secv4)
        if optiune == 6:
            f = True
main()
