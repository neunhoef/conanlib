#include <iostream>

#include "conanlib.h"

int main(int argc, char* argv[]) {
  std::cout << "Hello world!" << std::endl;
  int a = conanfunc(atoi(argv[1]));
  std::cout << "conanfunc: " << a << std::endl;
  return 0;
}
