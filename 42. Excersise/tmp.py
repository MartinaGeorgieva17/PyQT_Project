def foo(*args, **kw):
    print(args)
    print(kw)

foo()
foo(1,2,parent=3)