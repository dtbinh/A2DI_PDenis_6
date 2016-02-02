# A2DI_PDenis_6

Instructions sur http://researchers.lille.inria.fr/~pdenis/hw-online.txt

### Question 1

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u perc -i 1
Binary Classification model: perc
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.357143 	time = 0:00:00
done in 0:00:00
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.62 (8/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |      0.875      0.636      0.737 |          7         11          8
        -1 |        0.2        0.5      0.286 |          1          2          5
--------------------------------------------------------------------------------
```

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u perc -i 4
Binary Classification model: perc
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.357143 	time = 0:00:00
it.   1       14	avg loss = 0.5     	time = 0:00:00
it.   2       14	avg loss = 0.5     	time = 0:00:00
it.   3       14	avg loss = 0.285714 	time = 0:00:00
done in 0:00:00
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.85 (11/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |      0.875      0.875      0.875 |          7          8          8
        -1 |        0.8        0.8        0.8 |          4          5          5
--------------------------------------------------------------------------------
```

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u perc -i 10
Binary Classification model: perc
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.357143 	time = 0:00:00
it.   1       14	avg loss = 0.5     	time = 0:00:00
it.   2       14	avg loss = 0.5     	time = 0:00:00
it.   3       14	avg loss = 0.285714 	time = 0:00:00
it.   4       14	avg loss = 0.142857 	time = 0:00:00
it.   5       14	avg loss = 0.285714 	time = 0:00:00
it.   6       14	avg loss = 0.0     	time = 0:00:00
it.   7       14	avg loss = 0.0     	time = 0:00:00
it.   8       14	avg loss = 0.0     	time = 0:00:00
it.   9       14	avg loss = 0.0     	time = 0:00:00
done in 0:00:00
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.69 (9/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |       0.75       0.75       0.75 |          6          8          8
        -1 |        0.6        0.6        0.6 |          3          5          5
--------------------------------------------------------------------------------
```

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u perc -i 100
Binary Classification model: perc
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.357143 	time = 0:00:00
it.   1       14	avg loss = 0.5     	time = 0:00:00
it.   2       14	avg loss = 0.5     	time = 0:00:00
it.   3       14	avg loss = 0.285714 	time = 0:00:00
it.   4       14	avg loss = 0.142857 	time = 0:00:00
it.   5       14	avg loss = 0.285714 	time = 0:00:00
it.   6       14	avg loss = 0.0     	time = 0:00:00
it.   7       14	avg loss = 0.0     	time = 0:00:00
it.   8       14	avg loss = 0.0     	time = 0:00:00
it.   9       14	avg loss = 0.0     	time = 0:00:00
it.  10       14	avg loss = 0.0     	time = 0:00:00
it.  11       14	avg loss = 0.0     	time = 0:00:00
it.  12       14	avg loss = 0.0     	time = 0:00:00
...
it.  90       14	avg loss = 0.0     	time = 0:00:00
it.  91       14	avg loss = 0.0     	time = 0:00:00
it.  92       14	avg loss = 0.0     	time = 0:00:00
it.  93       14	avg loss = 0.0     	time = 0:00:00
it.  94       14	avg loss = 0.0     	time = 0:00:00
it.  95       14	avg loss = 0.0     	time = 0:00:00
it.  96       14	avg loss = 0.0     	time = 0:00:00
it.  97       14	avg loss = 0.0     	time = 0:00:00
it.  98       14	avg loss = 0.0     	time = 0:00:00
it.  99       14	avg loss = 0.0     	time = 0:00:00
done in 0:00:00
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.69 (9/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |       0.75       0.75       0.75 |          6          8          8
        -1 |        0.6        0.6        0.6 |          3          5          5
--------------------------------------------------------------------------------
```

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u perc -i 5000
Binary Classification model: perc
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.357143 	time = 0:00:00
it.   1       14	avg loss = 0.5     	time = 0:00:00
it.   2       14	avg loss = 0.5     	time = 0:00:00
it.   3       14	avg loss = 0.285714 	time = 0:00:00
it.   4       14	avg loss = 0.142857 	time = 0:00:00
it.   5       14	avg loss = 0.285714 	time = 0:00:00
it.   6       14	avg loss = 0.0     	time = 0:00:00
it.   7       14	avg loss = 0.0     	time = 0:00:00
it.   8       14	avg loss = 0.0     	time = 0:00:00
it.   9       14	avg loss = 0.0     	time = 0:00:00
...
it. 4990      14	avg loss = 0.0     	time = 0:00:00
it. 4991      14	avg loss = 0.0     	time = 0:00:00
it. 4992      14	avg loss = 0.0     	time = 0:00:00
it. 4993      14	avg loss = 0.0     	time = 0:00:00
it. 4994      14	avg loss = 0.0     	time = 0:00:00
it. 4995      14	avg loss = 0.0     	time = 0:00:00
it. 4996      14	avg loss = 0.0     	time = 0:00:00
it. 4997      14	avg loss = 0.0     	time = 0:00:00
it. 4998      14	avg loss = 0.0     	time = 0:00:00
it. 4999      14	avg loss = 0.0     	time = 0:00:00
done in 0:00:01
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.69 (9/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |       0.75       0.75       0.75 |          6          8          8
        -1 |        0.6        0.6        0.6 |          3          5          5
--------------------------------------------------------------------------------
```

### Question 2

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u pa -i 5
Binary Classification model: pa
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.915963 	time = 0:00:00
it.   1       14	avg loss = 0.799224 	time = 0:00:00
it.   2       14	avg loss = 0.65894 	time = 0:00:00
it.   3       14	avg loss = 0.551289 	time = 0:00:00
it.   4       14	avg loss = 0.48065 	time = 0:00:00
done in 0:00:00
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.92 (12/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |      0.875        1.0      0.933 |          7          7          8
        -1 |        1.0      0.833      0.909 |          5          6          5
--------------------------------------------------------------------------------
```

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u pa -i 10
Binary Classification model: pa
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.915963 	time = 0:00:00
it.   1       14	avg loss = 0.799224 	time = 0:00:00
it.   2       14	avg loss = 0.65894 	time = 0:00:00
it.   3       14	avg loss = 0.551289 	time = 0:00:00
it.   4       14	avg loss = 0.48065 	time = 0:00:00
it.   5       14	avg loss = 0.446881 	time = 0:00:00
it.   6       14	avg loss = 0.428057 	time = 0:00:00
it.   7       14	avg loss = 0.408499 	time = 0:00:00
it.   8       14	avg loss = 0.389525 	time = 0:00:00
it.   9       14	avg loss = 0.371429 	time = 0:00:00
done in 0:00:00
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.85 (11/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |       0.75        1.0      0.857 |          6          6          8
        -1 |        1.0      0.714      0.833 |          5          7          5
--------------------------------------------------------------------------------
```

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u pa -i 100
Binary Classification model: pa
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.915963 	time = 0:00:00
it.   1       14	avg loss = 0.799224 	time = 0:00:00
it.   2       14	avg loss = 0.65894 	time = 0:00:00
it.   3       14	avg loss = 0.551289 	time = 0:00:00
it.   4       14	avg loss = 0.48065 	time = 0:00:00
it.   5       14	avg loss = 0.446881 	time = 0:00:00
it.   6       14	avg loss = 0.428057 	time = 0:00:00
it.   7       14	avg loss = 0.408499 	time = 0:00:00
it.   8       14	avg loss = 0.389525 	time = 0:00:00
it.   9       14	avg loss = 0.371429 	time = 0:00:00
it.  10       14	avg loss = 0.354182 	time = 0:00:00
...
it.  90       14	avg loss = 0.007753 	time = 0:00:00
it.  91       14	avg loss = 0.007391 	time = 0:00:00
it.  92       14	avg loss = 0.007046 	time = 0:00:00
it.  93       14	avg loss = 0.006718 	time = 0:00:00
it.  94       14	avg loss = 0.006404 	time = 0:00:00
it.  95       14	avg loss = 0.006105 	time = 0:00:00
it.  96       14	avg loss = 0.005821 	time = 0:00:00
it.  97       14	avg loss = 0.005549 	time = 0:00:00
it.  98       14	avg loss = 0.00529 	time = 0:00:00
it.  99       14	avg loss = 0.005043 	time = 0:00:00
done in 0:00:00
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.77 (10/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |       0.75      0.857        0.8 |          6          7          8
        -1 |        0.8      0.667      0.727 |          4          6          5
--------------------------------------------------------------------------------
```

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u pa -i 5000
Binary Classification model: pa
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.915963 	time = 0:00:00
it.   1       14	avg loss = 0.799224 	time = 0:00:00
it.   2       14	avg loss = 0.65894 	time = 0:00:00
it.   3       14	avg loss = 0.551289 	time = 0:00:00
it.   4       14	avg loss = 0.48065 	time = 0:00:00
it.   5       14	avg loss = 0.446881 	time = 0:00:00
it.   6       14	avg loss = 0.428057 	time = 0:00:00
it.   7       14	avg loss = 0.408499 	time = 0:00:00
it.   8       14	avg loss = 0.389525 	time = 0:00:00
it.   9       14	avg loss = 0.371429 	time = 0:00:00
it.  10       14	avg loss = 0.354182 	time = 0:00:00

...
it. 286       14	avg loss = 1e-06   	time = 0:00:00
it. 287       14	avg loss = 1e-06   	time = 0:00:00
it. 288       14	avg loss = 1e-06   	time = 0:00:00
it. 289       14	avg loss = 1e-06   	time = 0:00:00
it. 290       14	avg loss = 1e-06   	time = 0:00:00
it. 291       14	avg loss = 1e-06   	time = 0:00:00
it. 292       14	avg loss = 0.0     	time = 0:00:00
it. 293       14	avg loss = 0.0     	time = 0:00:00
it. 294       14	avg loss = 0.0     	time = 0:00:00
it. 295       14	avg loss = 0.0     	time = 0:00:00
it. 296       14	avg loss = 0.0     	time = 0:00:00
...
it. 4990      14	avg loss = 0.0     	time = 0:00:00
it. 4991      14	avg loss = 0.0     	time = 0:00:00
it. 4992      14	avg loss = 0.0     	time = 0:00:00
it. 4993      14	avg loss = 0.0     	time = 0:00:00
it. 4994      14	avg loss = 0.0     	time = 0:00:00
it. 4995      14	avg loss = 0.0     	time = 0:00:00
it. 4996      14	avg loss = 0.0     	time = 0:00:00
it. 4997      14	avg loss = 0.0     	time = 0:00:00
it. 4998      14	avg loss = 0.0     	time = 0:00:00
it. 4999      14	avg loss = 0.0     	time = 0:00:00
done in 0:00:03
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.77 (10/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |       0.75      0.857        0.8 |          6          7          8
        -1 |        0.8      0.667      0.727 |          4          6          5
--------------------------------------------------------------------------------
```

#### Changement de C

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u pa -i 10 -C 0.35
Binary Classification model: pa
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.930657 	time = 0:00:00
it.   1       14	avg loss = 0.754507 	time = 0:00:00
it.   2       14	avg loss = 0.642208 	time = 0:00:00
it.   3       14	avg loss = 0.537676 	time = 0:00:00
it.   4       14	avg loss = 0.473679 	time = 0:00:00
it.   5       14	avg loss = 0.418825 	time = 0:00:00
it.   6       14	avg loss = 0.376875 	time = 0:00:00
it.   7       14	avg loss = 0.359364 	time = 0:00:00
it.   8       14	avg loss = 0.35169 	time = 0:00:00
it.   9       14	avg loss = 0.346008 	time = 0:00:00
done in 0:00:00
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.92 (12/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |      0.875        1.0      0.933 |          7          7          8
        -1 |        1.0      0.833      0.909 |          5          6          5
--------------------------------------------------------------------------------
```

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u pa -i 100 -C 0
Binary Classification model: pa
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 1.0     	time = 0:00:00
it.   1       14	avg loss = 1.0     	time = 0:00:00
it.   2       14	avg loss = 1.0     	time = 0:00:00
it.   3       14	avg loss = 1.0     	time = 0:00:00
it.   4       14	avg loss = 1.0     	time = 0:00:00
it.   5       14	avg loss = 1.0     	time = 0:00:00
it.   6       14	avg loss = 1.0     	time = 0:00:00
it.   7       14	avg loss = 1.0     	time = 0:00:00
it.   8       14	avg loss = 1.0     	time = 0:00:00
it.   9       14	avg loss = 1.0     	time = 0:00:00
...
it.  90       14	avg loss = 1.0     	time = 0:00:00
it.  91       14	avg loss = 1.0     	time = 0:00:00
it.  92       14	avg loss = 1.0     	time = 0:00:00
it.  93       14	avg loss = 1.0     	time = 0:00:00
it.  94       14	avg loss = 1.0     	time = 0:00:00
it.  95       14	avg loss = 1.0     	time = 0:00:00
it.  96       14	avg loss = 1.0     	time = 0:00:00
it.  97       14	avg loss = 1.0     	time = 0:00:00
it.  98       14	avg loss = 1.0     	time = 0:00:00
it.  99       14	avg loss = 1.0     	time = 0:00:00
done in 0:00:00
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.38 (5/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |        0.0        0.0        0.0 |          0          0          8
        -1 |        1.0      0.385      0.556 |          5         13          5
--------------------------------------------------------------------------------
```

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u pa -i 100 -C 10
Binary Classification model: pa
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.915963 	time = 0:00:00
it.   1       14	avg loss = 0.799224 	time = 0:00:00
it.   2       14	avg loss = 0.65894 	time = 0:00:00
it.   3       14	avg loss = 0.551289 	time = 0:00:00
it.   4       14	avg loss = 0.48065 	time = 0:00:00
it.   5       14	avg loss = 0.446881 	time = 0:00:00
it.   6       14	avg loss = 0.428057 	time = 0:00:00
it.   7       14	avg loss = 0.408499 	time = 0:00:00
it.   8       14	avg loss = 0.389525 	time = 0:00:00
it.   9       14	avg loss = 0.371429 	time = 0:00:00
...
it.  90       14	avg loss = 0.007753 	time = 0:00:00
it.  91       14	avg loss = 0.007391 	time = 0:00:00
it.  92       14	avg loss = 0.007046 	time = 0:00:00
it.  93       14	avg loss = 0.006718 	time = 0:00:00
it.  94       14	avg loss = 0.006404 	time = 0:00:00
it.  95       14	avg loss = 0.006105 	time = 0:00:00
it.  96       14	avg loss = 0.005821 	time = 0:00:00
it.  97       14	avg loss = 0.005549 	time = 0:00:00
it.  98       14	avg loss = 0.00529 	time = 0:00:00
it.  99       14	avg loss = 0.005043 	time = 0:00:00
done in 0:00:00
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.77 (10/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |       0.75      0.857        0.8 |          6          7          8
        -1 |        0.8      0.667      0.727 |          4          6          5
--------------------------------------------------------------------------------
```

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u pa -i 300 -C 1000
Binary Classification model: pa
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.915963 	time = 0:00:00
it.   1       14	avg loss = 0.799224 	time = 0:00:00
it.   2       14	avg loss = 0.65894 	time = 0:00:00
it.   3       14	avg loss = 0.551289 	time = 0:00:00
it.   4       14	avg loss = 0.48065 	time = 0:00:00
it.   5       14	avg loss = 0.446881 	time = 0:00:00
it.   6       14	avg loss = 0.428057 	time = 0:00:00
it.   7       14	avg loss = 0.408499 	time = 0:00:00
it.   8       14	avg loss = 0.389525 	time = 0:00:00
it.   9       14	avg loss = 0.371429 	time = 0:00:00
...
it. 287       14	avg loss = 1e-06   	time = 0:00:00
it. 288       14	avg loss = 1e-06   	time = 0:00:00
it. 289       14	avg loss = 1e-06   	time = 0:00:00
it. 290       14	avg loss = 1e-06   	time = 0:00:00
it. 291       14	avg loss = 1e-06   	time = 0:00:00
it. 292       14	avg loss = 0.0     	time = 0:00:00
it. 293       14	avg loss = 0.0     	time = 0:00:00
it. 294       14	avg loss = 0.0     	time = 0:00:00
it. 295       14	avg loss = 0.0     	time = 0:00:00
it. 296       14	avg loss = 0.0     	time = 0:00:00
it. 297       14	avg loss = 0.0     	time = 0:00:00
it. 298       14	avg loss = 0.0     	time = 0:00:00
it. 299       14	avg loss = 0.0     	time = 0:00:00
done in 0:00:00
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.77 (10/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |       0.75      0.857        0.8 |          6          7          8
        -1 |        0.8      0.667      0.727 |          4          6          5
--------------------------------------------------------------------------------
```

```
carette@b04p15:~/Documents/A2DI_PDenis_6$ python code-stub/py/polka/classification/binary.py -d code-stub/data/tennis/tennis.train -t code-stub/data/tennis/tennis.test -u pa -i 300 -C 0.25
Binary Classification model: pa
Training on data in 'code-stub/data/tennis/tennis.train'.
----------------------------------------------------------------------------------------------------
Training...
it.   0       14	avg loss = 0.933036 	time = 0:00:00
it.   1       14	avg loss = 0.699847 	time = 0:00:00
it.   2       14	avg loss = 0.618705 	time = 0:00:00
it.   3       14	avg loss = 0.53243 	time = 0:00:00
it.   4       14	avg loss = 0.46511 	time = 0:00:00
it.   5       14	avg loss = 0.415527 	time = 0:00:00
it.   6       14	avg loss = 0.382198 	time = 0:00:00
it.   7       14	avg loss = 0.348718 	time = 0:00:00
it.   8       14	avg loss = 0.317005 	time = 0:00:00
it.   9       14	avg loss = 0.299559 	time = 0:00:00
...
it. 287       14	avg loss = 1e-06   	time = 0:00:00
it. 288       14	avg loss = 1e-06   	time = 0:00:00
it. 289       14	avg loss = 1e-06   	time = 0:00:00
it. 290       14	avg loss = 1e-06   	time = 0:00:00
it. 291       14	avg loss = 1e-06   	time = 0:00:00
it. 292       14	avg loss = 1e-06   	time = 0:00:00
it. 293       14	avg loss = 1e-06   	time = 0:00:00
it. 294       14	avg loss = 1e-06   	time = 0:00:00
it. 295       14	avg loss = 1e-06   	time = 0:00:00
it. 296       14	avg loss = 1e-06   	time = 0:00:00
it. 297       14	avg loss = 1e-06   	time = 0:00:00
it. 298       14	avg loss = 1e-06   	time = 0:00:00
it. 299       14	avg loss = 1e-06   	time = 0:00:00
done in 0:00:00
done.
----------------------------------------------------------------------------------------------------
Testing... done in 0.001 sec.
====== ACC: 0.77 (10/13) ======
====== Recall/Precision/F1 by class labels ======
--------------------------------------------------------------------------------
     Label |     Recall   Precison         F1 |    Correct  Predicted       Gold
--------------------------------------------------------------------------------
         1 |       0.75      0.857        0.8 |          6          7          8
        -1 |        0.8      0.667      0.727 |          4          6          5
--------------------------------------------------------------------------------
```

### Question 3
