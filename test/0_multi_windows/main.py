from control.ctr_main import Ctr_Main
import multiprocessing

if __name__ == '__main__':
    multiprocessing.freeze_support()
    import sys
    ctrMain = Ctr_Main()
    sys.exit(main())
