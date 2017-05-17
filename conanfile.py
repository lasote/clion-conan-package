from conans import ConanFile, tools
from conans import CMake, AutoToolsBuildEnvironment


class LibpngConan(ConanFile):
    name = "libpng"
    version = "1.6.29"
    generators = "cmake", "txt"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    url="http://github.com/lasote/conan-libpng"
    requires = "zlib/1.2.11@lasote/stable"
    license = "Open source: http://www.libpng.org/pub/png/src/libpng-LICENSE.txt"
    description = "libpng is the official PNG reference library. It supports almost all PNG features, is extensible,"" \
    "" and has been extensively tested for over 20 years."
    exports_sources = "Find*.cmake", "source*"
    
    def configure(self):
        del self.settings.compiler.libcxx
        if self.settings.os == "Windows":
            self.options.remove("fPIC")
        

    def build(self):
        with tools.chdir("source"):
            cmake = CMake(self.settings)
            shared_options = "-DPNG_SHARED=ON -DPNG_STATIC=OFF" if self.options.shared else "-DPNG_SHARED=OFF -DPNG_STATIC=ON"

            self.run("mkdir _build")
            with tools.chdir("./_build"):
                self.run('cmake .. %s %s' % (cmake.command_line, shared_options))
                self.run("cmake --build . %s" % cmake.build_config)
                
    def package(self):
        """ Define your conan structure: headers, libs, bins and data. After building your
            project, this method is called to create a defined structure:
        """
        # Copy findPNG.cmake to package
        self.copy("FindPNG.cmake", ".", ".")

        # Copying headers
        self.copy("*.h", "include", "source", keep_path=False)

        # Copying static and dynamic libs
        if self.settings.os == "Windows":
            if self.options.shared:
                self.copy(pattern="*.dll", dst="bin", src="source", keep_path=False)
            self.copy(pattern="*.lib", dst="lib", src="source", keep_path=False)
        else:
            if self.options.shared:
                if self.settings.os == "Macos":
                    self.copy(pattern="*.dylib", dst="lib", keep_path=False, links=True)
                else:
                    self.copy(pattern="*.so*", dst="lib", src="source", keep_path=False, links=True)
            else:
                self.copy(pattern="*.a", dst="lib", src="source", keep_path=False, links=True)

    def package_info(self):
        if self.settings.os == "Windows":
            if self.options.shared:
                self.cpp_info.libs = ['libpng16']
            else:
                self.cpp_info.libs = ['libpng16_static']
            if self.settings.build_type == "Debug":
                self.cpp_info.libs[0] += "d"
        else:
            self.cpp_info.libs = ["png16"]
            if self.settings.os == "Linux":
                self.cpp_info.libs.append("m")
