"""
_______________.___.
\______   \__  |   |
 |    |  _//   |   |
 |    |   \\____   |
 |______  // ______|
        \/ \/       
   _____         _______           ________        __________.__         ._____________   __________ 
  /  _  \   ____ \   _  \   ____   \_____  \___  __\______   |  |   ____ |__\__    _______\______   \
 /  /_\  \ /    \/  /_\  \ /    \    _(__  <\  \/  /|     ___|  |  /  _ \|  | |    |_/ __ \|       _/
/    |    |   |  \  \_/   |   |  \  /       \>    < |    |   |  |_(  <_> |  | |    |\  ___/|    |   \
\____|__  |___|  /\_____  |___|  / /______  /__/\_ \|____|   |____/\____/|__| |____| \___  |____|_  /
        \/     \/       \/     \/         \/      \/                                     \/       \/ 

                                ~ Changing Coder Name Wont Make You One :)
                                             ~ An0n 3xPloiTeR :)
"""

import os

def installPackages(lib):
    import importlib
    try:
        importlib.import_module(lib)
    except ImportError:
        import pip
        pip.main(['install', lib])
    finally:
        try:
            globals()[lib] = importlib.import_module(lib)
        except ImportError, e:
            print "\nErr0r: Kindly Report This Error To Admin: \n", str(e)

pack = ["colorama", "os"]

for packages in pack:
    installPackages(packages)

from colorama import init,Fore,Back,Style


if os.name == "posix":
    # colors foreground text:
    fc = "\033[0;96m"
    fg = "\033[0;92m"
    fw = "\033[0;97m"
    fr = "\033[0;91m"
    fb = "\033[0;94m"
    fy = "\033[0;33m"
    fm = "\033[0;35m"

    # colors background text:
    bc = "\033[46m"
    bg = "\033[42m"
    bw = "\033[47m"
    br = "\033[41m"
    bb = "\033[44m"
    by = "\033[43m"
    bm = "\033[45m"

    # colors style text:
    sd = Style.DIM
    sn = Style.NORMAL
    sb = Style.BRIGHT

    c = fc + sb
    g = fg + sb
    w = fw + sb
    r = fr + sb
    b = fb + sb
    y = fy + sb
    m = fm + sb
else:
    ## ----------------------------------------------------------------------------------------------------------------------  ##
    init(autoreset=True)
    # colors foreground text:
    fc = Fore.CYAN
    fg = Fore.GREEN
    fw = Fore.WHITE
    fr = Fore.RED
    fb = Fore.BLUE
    fy = Fore.YELLOW
    fm = Fore.MAGENTA
    

    # colors background text:
    bc = Back.CYAN
    bg = Back.GREEN
    bw = Back.WHITE
    br = Back.RED
    bb = Back.BLUE
    by = Fore.YELLOW
    bm = Fore.MAGENTA

    # colors style text:
    sd = Style.DIM
    sn = Style.NORMAL
    sb = Style.BRIGHT

    c = fc + sb
    g = fg + sb
    w = fw + sb
    r = fr + sb
    b = fb + sb
    y = fy + sb
    m = fm + sb
    ## ----------------------------------------------------------------------------------------------------------------------  ##