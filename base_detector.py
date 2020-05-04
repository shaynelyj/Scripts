while 1:
    print "\nBase64: A-Z, a-z, 0-9, +/=. Max 2 '='"
    print "Base32: A-Z, 2-7. Max 6 '='"
    print "Base58: A-Z, a-z, 1-9 except (0OIl)"
    print "Base85: All except vwxy{}|"
    print "Base91: All except -\\'\n"
    a = raw_input("String: ")
    print "\n"

    Base58="0OIl"
    Base85="vwxy{}|"
    Base91="-\\'"

    for _ in Base58:
        if _ in a:
            print "Not Base58"
            break

    for _ in Base85:
        if _ in a:
            print "Not Base85"
            break

    for _ in Base91:
        if _ in a:
            print "Not Base91"
            break 
