#!/usr/bin/python

import urllib
import threading
import tarfile
import os
from subprocess import call
from os.path import expanduser

def read_file(filepath):
    dictionary = dict()
    for line in open(filepath):
        key, value = line.split()
        dictionary[key.strip()] = value.strip() 
    
    return dictionary

def download_modules(modules_dict):
    print "Downloading modules"
    for (module_name, url) in modules_dict.iteritems():
        # TODO: Check for errors
        filename = url.split('/')[-1]
        # TODO: Include checksum in config file to verify
        # TODO: Pretty print in tabular format
        print "[%s] from %s ..." % (module_name, url)
        urllib.urlretrieve(url, filename)

    print "Completed downloading modules\n"

def extract_modules(modules_dict):
    print "Extracting modules"
    for (module_name, url) in modules_dict.iteritems():
	    # TODO: Can use key/value pair in the config file
        # TODO: Check if the file exists 
        filename = url.split('/')[-1]
        print "[%s] from %s ..." % (module_name, filename)
        tar = tarfile.open(filename)
        tar.extractall()
        tar.close()
        folder_name = filename.strip(".tar.gz")

    print "Completed extracting modules\n"

def install_apr(apr_path):
    # TODO: Create class and move methods inside class so 
    #       that common variables like home, etc. can be abstracted
    print "Installing apr"
    home = expanduser("~")
    libpath = home+"/lib/apr"
    prefix = "--prefix="+libpath
    arguments=[]
    arguments.append(prefix)
    configure_make_install(apr_path, arguments)

def install_apr_util(apr_util_path, apr_path):
    print "Installing apr-util"
    home = expanduser("~")
    libpath = home+"/lib/apr-util"
    # TODO: Is there a better way to denote the arguments, 
    #       rather than string concat?
    prefix = "--prefix=" + libpath
    with_apr = "--with-apr=" + apr_path
    arguments=[]
    arguments.append(prefix)
    arguments.append(with_apr)
    configure_make_install(apr_path, arguments)

def install_pcre(pcre_path):
    print "Installing pcre"
    home = expanduser("~")
    libpath = home+"/lib/pcre"
    prefix = "--prefix="+libpath
    arguments=[]
    arguments.append(prefix)
    configure_make_install(pcre_path, arguments)

def install_httpd(httpd_path, apr_path, apr_util_path, pcre_path):
    print "Installing httpd"
    home = expanduser("~")
    libpath = home+"/apache"
    prefix = "--prefix="+libpath
    with_apr = "--with-apr=" + apr_path
    with_apr_util = "--with-apr-util=" + apr_util_path
    with_pcre = "--with-pcre=" + pcre_path
    arguments=[]
    arguments.append(prefix)
    arguments.append(with_apr)
    arguments.append(with_apr_util)
    arguments.append(with_pcre)
    configure_make_install(httpd_path, arguments)

def configure_make_install(source_path, configure_arguments):
    saved_path = os.getcwd()
    os.chdir(source_path);
    
    call(configure_arguments.insert(0, "./configure")
    call("make")
    call(["make", "install"])

    os.chdir(saved_path)

def get_folder_path(modules_dict, module_name):
    ext = ".tar.gz"
    filename = modules_dict[module_name].split('/')[-1]
    if filename.endswith(ext):
        return filename[:-len(ext)]

def install_modules(config_filepath):
    # TODO: Add unit tests
    modules_dict = read_file(config_filepath)
    download_modules(modules_dict)
    extract_modules(modules_dict)

    apr_path = get_folder_path(modules_dict, "apr")
    install_apr(apr_path)

    apr_util_path = get_folder_path("apr-util")
    install_apr_util(apr_util_path)

    pcre_path = get_folder_path("pcre")
    install_pcre(pcre_path)
    
    httpd_path = get_folder_path("httpd")
    install_httpd(httpd_path)

install_modules("download_config")