CLion Conan Example
===================

This repository contains a Clion project with libpng 1.6.29 and conan support. 
Follow the [Clion integration guide](http://docs.conan.io/en/latest/integrations/clion.html)

Build the project with CLion
----------------------------

- Open this directory with CLion => File => Open.

- Install the **libpng** dependencies:

    - Go to ``cmake-build-debug`` folder and run:

      ```
          conan install ../ -s build_type=Debug
   
      ```

  It will install the **zlib** requirements and will generate a **conanbuildinfo.cmake** file. Repeat the process for the
  different build configurations specifing the settings accordingly.
  
  Now you can inspect/debug the **zlib.h** file, it will point to your conan local cache.
  
  
- Build with the CLion IDE normally.


Build/test the conan package
----------------------------

- Just invoke `conan test_package` command in the root folder

```
    conan test_package
    
```

- If you want to use the local conan funtcion ``package`` to see if everything looks fine in your conan package files:


```
    mkdir package && cd package
    conan package --build_folder=../cmake-build-debug ..
```

  This command will copy all the conan package files to the local ``package`` directory.
