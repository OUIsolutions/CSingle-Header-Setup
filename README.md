# CSingle-Header-Setup

This is a complete setup for you to build single header libs in C,
providing from unit tests, with side effect verification,
to creation of automatic examples and code Amalgamation


### Understanding the Props 
The **props.py** contains all the constants that wil be used when you run the
**build.py**, after clone the repo, read all the flags (it has coments explaning)


### Understanding the PIPEline

After cloning this repository on your machine, run the build with

~~~bash
python3 build.py
~~~

### Step 1 : Generating the Amalgamation

The first thing that will happen will be the generation of the Amalgamation file, the script will look in the **props.py** file and will generate the merge of the inclusion of everything from **STARTER** and save it in **OUTPUT**

### Step 2 : Generating the OutPuts Tests

The next step will be to generate the output of all tests that do not exist

it will go through the entire folder **TEST_FOLDER**(props.py) and will generate the outputs of all the tests (folders starting with **T_**), which will consist of saving the result in **expected.txt** and also save the modified version of the side_effect folder

If they already exist, it will skip output generation, unless **RECONSTRUCT**(props.py) is set to True

## Step 3: Executing the Test

Now the system will run the tests, it will go through the entire **TEST_FOLDER** folder and will run the tests for all the **T_** folders it finds, comparing the execution result with the **expected.txt** , as well as comparing the **SIDE_EFFECT_FOLDER** modifications


## Step 4 Creating the Exemples

In the example creation part, the system will go through the **TEST_FOLDER** and will copy all the files to /examples, also replacing the inclusion headers

## Step 5 Generating the Markdown

And finally, the system will replace the markdown code, replacing all **codeof** in **README.md** with your correct code

Exemple:
<!--codeof:exemples/calc/add.c-->
~~~c

#include "LibName.h"

int main(){
    double r = add(10,20);
    printf("%lf",r);
}
~~~

### Testing Locally 

for testing your code localy you can just import the start normal 

~~~c 
#include "src/start.h"

int main(){

}

~~~