// platform: beecrowd - https://judge.beecrowd.com/pt/problems/view/3128
// programming language: C++
// status: Accepted

// author: Gabriel Soares
// https://www.linkedin.com/in/gabrielsoarespebr/
// https://github.com/gabrielsoarespebr

#include <iostream>

using namespace std;

int main()
{
    int idadeFulano;
    int idadeCiclano;
    char *permissao = "YES";

    cin >> idadeFulano;
    cin >> idadeCiclano;

    if ((idadeFulano < 6) || (idadeCiclano < 6))
        permissao = "NO";

    if ((idadeFulano < 14) && (idadeCiclano < 18))
        permissao = "NO";

    if ((idadeFulano < 18) && (idadeCiclano < 14))
        permissao = "NO";

    cout << permissao << endl;

    return 0;
}