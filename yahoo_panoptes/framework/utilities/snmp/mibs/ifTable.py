ifTable = '.1.3.6.1.2.1.2.2.1'
ifDescr = ifTable + '.2'
ifType = ifTable + '.3'
ifMtu = ifTable + '.4'
ifSpeed = ifTable + '.5'
ifPhysAddress = ifTable + '.6'
ifAdminStatus = ifTable + '.7'
ifOperStatus = ifTable + '.8'
ifInDiscards = ifTable + '.13'
ifInErrors = ifTable + '.14'
ifOutDiscards = ifTable + '.19'
ifOutErrors = ifTable + '.20'

ifTypeEnum = [("other", 1), ("regular1822", 2), ("hdh1822", 3), ("ddnX25", 4), ("rfc877x25", 5), ("ethernetCsmacd", 6),
              ("iso88023Csmacd", 7), ("iso88024TokenBus", 8), ("iso88025TokenRing", 9), ("iso88026Man", 10),
              ("starLan", 11), ("proteon10Mbit", 12), ("proteon80Mbit", 13), ("hyperchannel", 14), ("fddi", 15),
              ("lapb", 16), ("sdlc", 17), ("ds1", 18), ("e1", 19), ("basicISDN", 20), ("primaryISDN", 21),
              ("propPointToPointSerial", 22), ("ppp", 23), ("softwareLoopback", 24), ("eon", 25), ("ethernet3Mbit", 26),
              ("nsip", 27), ("slip", 28), ("ultra", 29), ("ds3", 30), ("sip", 31), ("frameRelay", 32), ("rs232", 33),
              ("para", 34), ("arcnet", 35), ("arcnetPlus", 36), ("atm", 37), ("miox25", 38), ("sonet", 39),
              ("x25ple", 40), ("iso88022llc", 41), ("localTalk", 42), ("smdsDxi", 43), ("frameRelayService", 44),
              ("v35", 45), ("hssi", 46), ("hippi", 47), ("modem", 48), ("aal5", 49), ("sonetPath", 50), ("sonetVT", 51),
              ("smdsIcip", 52), ("propVirtual", 53), ("propMultiplexor", 54), ("ieee80212", 55), ("fibreChannel", 56),
              ("hippiInterface", 57), ("frameRelayInterconnect", 58), ("aflane8023", 59), ("aflane8025", 60),
              ("cctEmul", 61), ("fastEther", 62), ("isdn", 63), ("v11", 64), ("v36", 65), ("g703at64k", 66),
              ("g703at2mb", 67), ("qllc", 68), ("fastEtherFX", 69), ("channel", 70), ("ieee80211", 71),
              ("ibm370parChan", 72), ("escon", 73), ("dlsw", 74), ("isdns", 75), ("isdnu", 76), ("lapd", 77),
              ("ipSwitch", 78), ("rsrb", 79), ("atmLogical", 80), ("ds0", 81), ("ds0Bundle", 82), ("bsc", 83),
              ("async", 84), ("cnr", 85), ("iso88025Dtr", 86), ("eplrs", 87), ("arap", 88), ("propCnls", 89),
              ("hostPad", 90), ("termPad", 91), ("frameRelayMPI", 92), ("x213", 93), ("adsl", 94), ("radsl", 95),
              ("sdsl", 96), ("vdsl", 97), ("iso88025CRFPInt", 98), ("myrinet", 99), ("voiceEM", 100), ("voiceFXO", 101),
              ("voiceFXS", 102), ("voiceEncap", 103), ("voiceOverIp", 104), ("atmDxi", 105), ("atmFuni", 106),
              ("atmIma", 107), ("pppMultilinkBundle", 108), ("ipOverCdlc", 109), ("ipOverClaw", 110),
              ("stackToStack", 111), ("virtualIpAddress", 112), ("mpc", 113), ("ipOverAtm", 114),
              ("iso88025Fiber", 115), ("tdlc", 116), ("gigabitEthernet", 117), ("hdlc", 118), ("lapf", 119),
              ("v37", 120), ("x25mlp", 121), ("x25huntGroup", 122), ("transpHdlc", 123), ("interleave", 124),
              ("fast", 125), ("ip", 126), ("docsCableMaclayer", 127), ("docsCableDownstream", 128),
              ("docsCableUpstream", 129), ("a12MppSwitch", 130), ("tunnel", 131), ("coffee", 132), ("ces", 133),
              ("atmSubInterface", 134), ("l2vlan", 135), ("l3ipvlan", 136), ("l3ipxvlan", 137),
              ("digitalPowerline", 138), ("mediaMailOverIp", 139), ("dtm", 140), ("dcn", 141), ("ipForward", 142),
              ("msdsl", 143), ("ieee1394", 144), ("if-gsn", 145), ("dvbRccMacLayer", 146), ("dvbRccDownstream", 147),
              ("dvbRccUpstream", 148), ("atmVirtual", 149), ("mplsTunnel", 150), ("srp", 151), ("voiceOverAtm", 152),
              ("voiceOverFrameRelay", 153), ("idsl", 154), ("compositeLink", 155), ("ss7SigLink", 156),
              ("propWirelessP2P", 157), ("frForward", 158), ("rfc1483", 159), ("usb", 160), ("ieee8023adLag", 161),
              ("bgppolicyaccounting", 162), ("frf16MfrBundle", 163), ("h323Gatekeeper", 164), ("h323Proxy", 165),
              ("mpls", 166), ("mfSigLink", 167), ("hdsl2", 168), ("shdsl", 169), ("ds1FDL", 170), ("pos", 171),
              ("dvbAsiIn", 172), ("dvbAsiOut", 173), ("plc", 174), ("nfas", 175), ("tr008", 176), ("gr303RDT", 177),
              ("gr303IDT", 178), ("isup", 179), ("propDocsWirelessMaclayer", 180), ("propDocsWirelessDownstream", 181),
              ("propDocsWirelessUpstream", 182), ("hiperlan2", 183), ("propBWAp2Mp", 184),
              ("sonetOverheadChannel", 185), ("digitalWrapperOverheadChannel", 186), ("aal2", 187), ("radioMAC", 188),
              ("atmRadio", 189), ("imt", 190), ("mvl", 191), ("reachDSL", 192), ("frDlciEndPt", 193),
              ("atmVciEndPt", 194), ("opticalChannel", 195), ("opticalTransport", 196), ("propAtm", 197),
              ("voiceOverCable", 198), ("infiniband", 199), ("teLink", 200), ("q2931", 201), ("virtualTg", 202),
              ("sipTg", 203), ("sipSig", 204), ("docsCableUpstreamChannel", 205), ("econet", 206), ("pon155", 207),
              ("pon622", 208), ("bridge", 209), ("linegroup", 210), ("voiceEMFGD", 211), ("voiceFGDEANA", 212),
              ("voiceDID", 213), ("mpegTransport", 214), ("sixToFour", 215), ("gtp", 216), ("pdnEtherLoop1", 217),
              ("pdnEtherLoop2", 218), ("opticalChannelGroup", 219), ("homepna", 220), ("gfp", 221),
              ("ciscoISLvlan", 222), ("actelisMetaLOOP", 223), ("fcipLink", 224), ("rpr", 225), ("qam", 226),
              ("lmp", 227), ("cblVectaStar", 228), ("docsCableMCmtsDownstream", 229), ("adsl2", 230),
              ("macSecControlledIF", 231), ("macSecUncontrolledIF", 232), ("aviciOpticalEther", 233), ("atmbond", 234),
              ("voiceFGDOS", 235), ("mocaVersion1", 236), ("ieee80216WMAN", 237), ("adsl2plus", 238),
              ("dvbRcsMacLayer", 239), ("dvbTdm", 240), ("dvbRcsTdma", 241), ("x86Laps", 242), ("wwanPP", 243),
              ("wwanPP2", 244), ("voiceEBS", 245), ("ifPwType", 246), ("ilan", 247), ("pip", 248), ("aluELP", 249),
              ("gpon", 250), ("vdsl2", 251)]


if_table_oids = [ifMtu, ifSpeed, ifAdminStatus, ifPhysAddress, ifOperStatus, ifInErrors, ifOutErrors,
                 ifInDiscards, ifOutDiscards]


def getIfTypeDesc(ifType):
    return ifTypeEnum[int(ifType) - 1][0]
