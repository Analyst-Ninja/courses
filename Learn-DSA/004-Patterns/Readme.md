### Patterns Code

#### Square Patterns

```c++
// Square with Numbers

#include <iostream>
using namespace std;


int main() {

    int n = 5;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << j << " ";
        }
        cout << endl;
    }

}

// Output
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
```

```c++
// Square with Alphabets

#include <iostream>
using namespace std;

int main() {

    int n = 5;
    for (int i = 1; i <= n; i++) {
        char ch = 'A';
        for (int j = 1; j <= n; j++) {
            cout << ch << " ";
            ch++;
        }
        cout << endl;
    }
};

// Output
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
```

```c++
// Square with numbers continously increasing

int main() {

    int n = 3;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            sum++;
            cout << sum << " ";
        }
        cout << endl;
    }
};

// Output
1 2 3
4 5 6
7 8 9
```

```c++
// Square Pattern with Alphabets continously increasing

int main() {

    int n = 5;
    char ch = 'A';
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << ch << " ";
            ch++;
        }
        cout << endl;
    }
};

// Output
A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y
```

#### Triangle Patterns

```c++
int main() {
    // Left Triangle Pattern
    int n = 5;

    for (int i = 0; i < n; i++ ) {
        for (int j = 0; j <= i; j++ ) {
            cout << "* ";
        }
        cout << endl;
    }
};

// Output
*
* *
* * *
* * * *
* * * * *
```

```c++
int main() {
    // Left Triangle Pattern with Characters
    char ch = 'A';

    for (int i = 0; i < n; i++ ) {
        for (int j = 0; j <= i; j++ ) {
            cout << ch + i << " ";
        }
        cout << endl;
    }
};

// Output
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

```c++
int main() {
    // Left Triangle Pattern with Alphabets
    char ch = 'A';
    int n = 5;

    for (int i = 0; i < n; i++ ) {
        for (int j = 0; j <= i; j++ ) {
            char charToPrint = ch + i;
            cout << charToPrint << " ";
        }
        cout << endl;
    }
};

// Output
A
B B
C C C
D D D D
E E E E E
```

```c++
int main() {
    // Left Triangle Pattern with Numbers increasing
    int n = 5;

    for (int i = 0; i < n; i++ ) {
        for (int j = 0; j <= i; j++ ) {
            cout << j+1 << " ";
        }
        cout << endl;
    }
};

// Output
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

```c++
int main() {
    // Left Triangle Pattern with Numbers in reverse
    int n = 5;

    for (int i = 0; i < n; i++) {
        for (int j = i+1; j > 0; j--) {
            cout << j << " ";
        }
        cout << endl;
    }

};

// Output
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
```

```c++
int main() {
    // Left Triangle with Character in reverse
    int n = 5;
    char ch = 'A';

    for (int i = 0; i < n; i++) {
        for (int j = i+1; j > 0; j--) {
            char charToPrint = ch+j-1;
            cout << charToPrint << " ";
        }
        cout << endl;
    }

};

// Output
A
B A
C B A
D C B A
E D C B A
```

```c++
int main() {
    // Floyd's Triangle with Numbers
    int n = 4;
    int sum = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            sum++;
            cout << sum << " ";
        }
        cout << endl;
    }

};

// Output
1
2 3
4 5 6
7 8 9 10
```

```c++
int main() {
    // Floyd's Triangle with Characters
    int n = 5;
    char ch = 'A';

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cout << ch << " ";
            ch++;
        }
        cout << endl;
    }

};

// Output
A
B C
D E F
G H I J
K L M N O
```

```c++
int main() {
    // Inverted Triangle with number same in a row but increasing by each row
    int n = 5;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j < i) {
                cout << " ";
            } else {
                cout << i+1;
            }
        }
        cout << endl;
    }

};

// Output
11111
 2222
  333
   44
    5
```

```c++
int main() {
    // Inverted Triangle with number same in a row but increasing by each row
    // Alternative
    int n = 5;

    for (int i = 0; i < n; i++) {

        // spaces
        for (int j = 0; j < i; j++) {
            cout << " ";
        }
        // nums
        for (int k = 0; k < n-i; k++) {
            cout << i+1;
        }
        cout << endl;
    }

};

// Output
11111
 2222
  333
   44
    5
```

```c++

int main() {
    // Hollow diamond pattern
    int n = 6;

    // Upper Part
    for (int i=0; i < n; i++){
        for (int j=0; j < n; j++) {
            if (j == n-i-1) {
                cout << "*";
            }
            else {
                cout << " ";
            }
        }
        for (int j=0; j < n - 1; j++) {
            if (j == i - 1) {
                cout << "*";
            } else {
                cout << " ";
            }
        }

    cout << endl;
    }

    //Lower Part
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n; j++) {
            if (i + 1 == j) {
                cout << "*";
            } else {
                cout << " ";
            }
        }
        for (int j = 0; j < n - 1; j++) {
            if (j == n - i - 3) {
                cout << "*";
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
};

//Output
     *
    * *
   *   *
  *     *
 *       *
*         *
 *       *
  *     *
   *   *
    * *
     *
```

```c++
int main() {
    // Butterfly Pattern
    int n = 4;
    for (int i=0; i<n; i++) {
        for(int j=0; j<=i; j++) {
            cout << "*";
        }

        for (int j=0; j<2*n-2*i-2; j++) {
            if (i!=n-1) {
                cout << " ";
            }
        }

        for(int j=0; j<=i; j++) {
            cout << "*";
        }

        cout << endl;
    }

    for (int i=0; i<n; i++){
        for (int j=n; j>i; j--) {
            cout << "*";
        }
        for (int j=0; j<2*i; j++) {
                if (i!=0) {
                    cout << " ";
                }
            }
        for (int j=n; j>i; j--) {
            if (j!=0) {
                cout << "*";
            }
        }
        cout << endl;
    }

};

// Output
*      *
**    **
***  ***
********
********
***  ***
**    **
*      *
```
