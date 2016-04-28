"""Blacklist particular articles from doing particular activities"""

def publication_email_article_do_not_send_list():
    """
    Return list of do not send article DOI id
    """

    do_not_send_list = [
        "00003", "00005", "00007", "00011", "00012", "00013", "00031", "00036", "00047", "00048",
        "00049", "00051", "00065", "00067", "00068", "00070", "00078", "00090", "00093", "00102",
        "00105", "00109", "00116", "00117", "00133", "00160", "00170", "00171", "00173", "00178",
        "00181", "00183", "00184", "00190", "00205", "00218", "00220", "00230", "00231", "00240",
        "00242", "00243", "00247", "00248", "00260", "00269", "00270", "00278", "00281", "00286",
        "00288", "00290", "00291", "00299", "00301", "00302", "00306", "00308", "00311", "00312",
        "00321", "00324", "00326", "00327", "00329", "00333", "00334", "00336", "00337", "00340",
        "00347", "00348", "00351", "00352", "00353", "00354", "00358", "00362", "00365", "00367",
        "00378", "00380", "00385", "00386", "00387", "00400", "00411", "00415", "00421", "00422",
        "00425", "00426", "00429", "00435", "00444", "00450", "00452", "00458", "00459", "00461",
        "00467", "00471", "00473", "00475", "00476", "00477", "00481", "00482", "00488", "00491",
        "00498", "00499", "00505", "00508", "00515", "00518", "00522", "00523", "00533", "00534",
        "00537", "00542", "00558", "00563", "00565", "00569", "00571", "00572", "00573", "00577",
        "00590", "00592", "00593", "00594", "00603", "00605", "00615", "00625", "00626", "00631",
        "00632", "00633", "00638", "00639", "00640", "00641", "00642", "00646", "00647", "00648",
        "00654", "00655", "00658", "00659", "00662", "00663", "00666", "00668", "00669", "00672",
        "00675", "00676", "00683", "00691", "00692", "00699", "00704", "00708", "00710", "00712",
        "00723", "00726", "00729", "00731", "00736", "00744", "00745", "00747", "00750", "00757",
        "00759", "00762", "00767", "00768", "00772", "00776", "00778", "00780", "00782", "00785",
        "00790", "00791", "00792", "00799", "00800", "00801", "00802", "00804", "00806", "00808",
        "00813", "00822", "00824", "00825", "00828", "00829", "00842", "00844", "00845", "00855",
        "00856", "00857", "00861", "00862", "00863", "00866", "00868", "00873", "00882", "00884",
        "00886", "00895", "00899", "00903", "00905", "00914", "00924", "00926", "00932", "00933",
        "00940", "00943", "00947", "00948", "00951", "00953", "00954", "00958", "00960", "00961",
        "00963", "00966", "00967", "00969", "00971", "00983", "00992", "00994", "00996", "00999",
        "01004", "01008", "01009", "01020", "01029", "01030", "01042", "01045", "01061", "01064",
        "01067", "01071", "01074", "01084", "01085", "01086", "01089", "01096", "01098", "01102",
        "01104", "01108", "01114", "01115", "01119", "01120", "01123", "01127", "01133", "01135",
        "01136", "01138", "01139", "01140", "01149", "01157", "01159", "01160", "01169", "01179",
        "01180", "01197", "01201", "01202", "01206", "01211", "01213", "01214", "01221", "01222",
        "01228", "01229", "01233", "01234", "01236", "01239", "01252", "01256", "01257", "01267",
        "01270", "01273", "01279", "01287", "01289", "01291", "01293", "01294", "01295", "01296",
        "01298", "01299", "01305", "01308", "01310", "01311", "01312", "01319", "01322", "01323",
        "01326", "01328", "01339", "01340", "01341", "01345", "01350", "01355", "01369", "01370",
        "01374", "01381", "01385", "01386", "01387", "01388", "01402", "01403", "01412", "01414",
        "01426", "01428", "01433", "01434", "01438", "01439", "01440", "01456", "01457", "01460",
        "01462", "01465", "01469", "01473", "01479", "01481", "01482", "01483", "01488", "01489",
        "01494", "01496", "01498", "01501", "01503", "01514", "01515", "01516", "01519", "01524",
        "01530", "01535", "01539", "01541", "01557", "01561", "01566", "01567", "01569", "01574",
        "01579", "01581", "01584", "01587", "01596", "01597", "01599", "01603", "01604", "01605",
        "01607", "01608", "01610", "01612", "01621", "01623", "01630", "01632", "01633", "01637",
        "01641", "01658", "01659", "01662", "01663", "01671", "01680", "01681", "01684", "01694",
        "01695", "01699", "01700", "01710", "01715", "01724", "01730", "01738", "01739", "01741",
        "01749", "01751", "01754", "01760", "01763", "01775", "01776", "01779", "01808", "01809",
        "01812", "01816", "01817", "01820", "01828", "01831", "01832", "01833", "01834", "01839",
        "01845", "01846", "01849", "01856", "01857", "01861", "01867", "01873", "01879", "01883",
        "01888", "01892", "01893", "01901", "01906", "01911", "01913", "01914", "01916", "01917",
        "01926", "01928", "01936", "01939", "01944", "01948", "01949", "01958", "01963", "01964",
        "01967", "01968", "01977", "01979", "01982", "01990", "01993", "01998", "02001", "02008",
        "02009", "02020", "02024", "02025", "02028", "02030", "02040", "02041", "02042", "02043",
        "02046", "02053", "02057", "02061", "02062", "02069", "02076", "02077", "02078", "02087",
        "02088", "02094", "02104", "02105", "02109", "02112", "02115", "02130", "02131", "02137",
        "02148", "02151", "02152", "02164", "02171", "02172", "02181", "02184", "02189", "02190",
        "02196", "02199", "02200", "02203", "02206", "02208", "02217", "02218", "02224", "02230",
        "02236", "02238", "02242", "02245", "02252", "02257", "02260", "02265", "02270", "02272",
        "02273", "02277", "02283", "02286", "02289", "02304", "02313", "02322", "02324", "02349",
        "02362", "02365", "02369", "02370", "02372", "02375", "02384", "02386", "02387", "02391",
        "02394", "02395", "02397", "02403", "02407", "02409", "02419", "02439", "02440", "02443",
        "02444", "02445", "02450", "02451", "02475", "02478", "02481", "02482", "02490", "02501",
        "02504", "02510", "02511", "02515", "02516", "02517", "02523", "02525", "02531", "02535",
        "02536", "02555", "02557", "02559", "02564", "02565", "02576", "02583", "02589", "02590",
        "02598", "02615", "02618", "02619", "02626", "02630", "02634", "02637", "02641", "02653",
        "02658", "02663", "02667", "02669", "02670", "02671", "02674", "02676", "02678", "02687",
        "02715", "02725", "02726", "02730", "02734", "02736", "02740", "02743", "02747", "02750",
        "02755", "02758", "02763", "02772", "02777", "02780", "02784", "02786", "02791", "02792",
        "02798", "02805", "02809", "02811", "02812", "02813", "02833", "02839", "02840", "02844",
        "02848", "02851", "02854", "02860", "02862", "02863", "02866", "02872", "02875", "02882",
        "02893", "02897", "02904", "02907", "02910", "02917", "02923", "02935", "02938", "02945",
        "02949", "02950", "02951", "02956", "02963", "02964", "02975", "02978", "02981", "02993",
        "02996", "02999", "03005", "03007", "03011", "03023", "03025", "03031", "03032", "03035",
        "03043", "03058", "03061", "03068", "03069", "03075", "03077", "03080", "03083", "03091",
        "03100", "03104", "03110", "03115", "03116", "03125", "03126", "03128", "03145", "03146",
        "03159", "03164", "03176", "03178", "03180", "03185", "03191", "03197", "03198", "03205",
        "03206", "03222", "03229", "03233", "03235", "03239", "03245", "03251", "03254", "03255",
        "03271", "03273", "03275", "03282", "03285", "03293", "03297", "03300", "03307", "03311",
        "03318", "03342", "03346", "03348", "03351", "03357", "03363", "03371", "03372", "03374",
        "03375", "03383", "03385", "03397", "03398", "03399", "03401", "03405", "03406", "03416",
        "03421", "03422", "03427", "03430", "03433", "03435", "03440", "03443", "03464", "03467",
        "03468", "03473", "03475", "03476", "03487", "03496", "03497", "03498", "03502", "03504",
        "03521", "03522", "03523", "03526", "03528", "03532", "03542", "03545", "03549", "03553",
        "03558", "03563", "03564", "03568", "03573", "03574", "03575", "03579", "03581", "03582",
        "03583", "03587", "03596", "03600", "03602", "03604", "03606", "03609", "03613", "03626",
        "03635", "03638", "03640", "03641", "03648", "03650", "03653", "03656", "03658", "03663",
        "03665", "03671", "03674", "03676", "03678", "03679", "03680", "03683", "03695", "03696",
        "03697", "03701", "03702", "03703", "03706", "03711", "03714", "03720", "03722", "03724",
        "03726", "03727", "03728", "03735", "03737", "03743", "03751", "03753", "03754", "03756",
        "03764", "03765", "03766", "03772", "03778", "03779", "03781", "03785", "03790", "03804",
        "03811", "03819", "03821", "03830", "03842", "03848", "03851", "03868", "03881", "03883",
        "03891", "03892", "03895", "03896", "03908", "03915", "03925", "03939", "03941", "03943",
        "03949", "03952", "03962", "03970", "03971", "03977", "03978", "03980", "03981", "03997",
        "04000", "04006", "04008", "04014", "04024", "04034", "04037", "04040", "04046", "04047",
        "04057", "04059", "04066", "04069", "04070", "04094", "04105", "04106", "04111", "04114",
        "04120", "04121", "04123", "04126", "04132", "04135", "04137", "04147", "04158", "04165",
        "04168", "04177", "04180", "04187", "04193", "04205", "04207", "04220", "04234", "04235",
        "04236", "04246", "04247", "04249", "04251", "04263", "04265", "04266", "04273", "04279",
        "04287", "04288", "04300", "04316", "04333", "04353", "04363", "04366", "04371", "04378",
        "04380", "04387", "04389", "04390", "04395", "04402", "04406", "04415", "04418", "04433",
        "04437", "04449", "04476", "04478", "04489", "04491", "04494", "04499", "04501", "04506",
        "04517", "04525", "04530", "04531", "04534", "04543", "04551", "04553", "04563", "04565",
        "04577", "04580", "04581", "04586", "04591", "04600", "04601", "04603", "04605", "04617",
        "04629", "04630", "04631", "04645", "04660", "04664", "04686", "04692", "04693", "04711",
        "04729", "04741", "04742", "04766", "04775", "04779", "04785", "04801", "04806", "04811",
        "04851", "04854", "04869", "04875", "04876", "04878", "04885", "04889", "04901", "04902",
        "04909", "04919", "04969", "04970", "04986", "04995", "04996", "04997", "04998", "05000",
        "05007", "05025", "05031", "05033", "05041", "05048", "05055", "05060", "05075", "05087",
        "05105", "05115", "05116", "05125", "05151", "05161", "05169", "05178", "05179", "05198",
        "05216", "05218", "05244", "05256", "05259", "05269", "05289", "05290", "05334", "05352",
        "05375", "05377", "05394", "05401", "05418", "05419", "05422", "05427", "05438", "05490",
        "05504", "05508", "05553", "05558", "05564", "05570", "05580", "05597", "05614", "05657",
        "05663", "05720", "05770", "05787", "05789", "05816", "05846", "05896", "05983", "06156",
        "06193", "06200", "06235", "06303", "06306", "06351", "06424", "06430", "06453", "06494",
        "06656", "06720", "06740", "06900", "06986"]

    # More do not send circa July 2015
    #  Do not send email if they are revised, since the duplicate check will not
    #  trigger since they were not sent in the first place
    do_not_send_list = do_not_send_list + ["04186", "06416", "06847", "06938", "06959", "07072"]

    return do_not_send_list

def pub_router_deposit_article_blacklist(workflow):
    """
    Return list of do not send article DOI id
    """

    if workflow == "HEFCE":
        article_blacklist = [
            "00003", "00005", "00007", "00011", "00013",
            "00031", "00047", "00048", "00049", "00051",
            "00065", "00067", "00068", "00070", "00078",
            "00090", "00093", "00102", "00109", "00117",
            "00171", "00173", "00181", "00184", "00205",
            "00240", "00242", "00243", "00248", "00270",
            "00281", "00286", "00301", "00302", "00311",
            "00326", "00340", "00347", "00351", "00352",
            "00353", "00365", "00385", "00386", "00387",
            "00475", "00012", "00036", "00105", "00116",
            "00133", "00160", "00170", "00178", "00183",
            "00190", "00218", "00220", "00230", "00231",
            "00247", "00260", "00269", "00278", "00288",
            "00290", "00291", "00299", "00306", "00308",
            "00312", "00321", "00324", "00327", "00329",
            "00333", "00334", "00336", "00337", "00348",
            "00354", "00358", "00362", "00367", "00378",
            "00380", "00400", "00411", "00415", "00421",
            "00422", "00425", "00426", "00429", "00435",
            "00444", "00450", "00452", "00458", "00459",
            "00461", "00467", "00471", "00473", "00476",
            "00477", "00481", "00482", "00488", "00491",
            "00498", "00499", "00505", "00508", "00515",
            "00518", "00522", "00523", "00533", "00534",
            "00537", "00542", "00558", "00563", "00565",
            "00569", "00571", "00572", "00573", "00577",
            "00592", "00593", "00594", "00603", "00605",
            "00615", "00625", "00626", "00631", "00632",
            "00633", "00638", "00639", "00640", "00641",
            "00642", "00646", "00647", "00648", "00654",
            "00655", "00658", "00659", "00663", "00666",
            "00668", "00669", "00672", "00675", "00676",
            "00683", "00691", "00692", "00699", "00704",
            "00708", "00710", "00712", "00723", "00726",
            "00729", "00731", "00736", "00744", "00745",
            "00747", "00750", "00757", "00759", "00762",
            "00767", "00768", "00772", "00776", "00778",
            "00780", "00782", "00785", "00790", "00791",
            "00792", "00799", "00800", "00801", "00802",
            "00804", "00806", "00808", "00813", "00822",
            "00824", "00825", "00828", "00842", "00844",
            "00845", "00855", "00856", "00857", "00861",
            "00862", "00863", "00866", "00868", "00873",
            "00882", "00884", "00886", "00895", "00899",
            "00903", "00905", "00914", "00924", "00926",
            "00932", "00933", "00940", "00943", "00947",
            "00948", "00951", "00953", "00954", "00958",
            "00960", "00961", "00963", "00966", "00967",
            "00969", "00971", "00983", "00992", "00994",
            "00996", "00999", "01004", "01008", "01009",
            "01020", "01029", "01030", "01042", "01045",
            "01061", "01064", "01067", "01071", "01074",
            "01084", "01085", "01086", "01089", "01096",
            "01098", "01102", "01104", "01108", "01114",
            "01115", "01119", "01120", "01123", "01127",
            "01133", "01135", "01136", "01138", "01139",
            "01140", "01149", "01157", "01159", "01160",
            "01169", "01179", "01180", "01197", "01202",
            "01206", "01211", "01213", "01214", "01221",
            "01222", "01228", "01229", "01233", "01234",
            "01236", "01252", "01256", "01270", "01273",
            "01279", "01287", "01289", "01291", "01293",
            "01294", "01295", "01296", "01298", "01299",
            "01305", "01312", "01319", "01323", "01326",
            "01328", "01339", "01340", "01341", "01345",
            "01350", "01387", "01388", "01402", "01403",
            "01414", "01426", "01428", "01456", "01462",
            "01469", "01482", "01494", "01501", "01503",
            "01514", "01515", "01516", "01519", "01541",
            "01557", "01561", "01574", "01587", "01597",
            "01599", "01605", "01608", "01633", "01658",
            "01662", "01663", "01680", "01700", "01710",
            "01738", "01749", "01760", "01779", "01809",
            "01816", "01820", "01839", "01845", "01873",
            "01893", "01926", "01968", "01979", "02094",
            "00590", "00662", "00829", "01201", "01239",
            "01257", "01267", "01308", "01310", "01311",
            "01322", "01355", "01369", "01370", "01374",
            "01381", "01385", "01386", "01412", "01433",
            "01434", "01438", "01439", "01440", "01457",
            "01460", "01465", "01473", "01479", "01481",
            "01483", "01488", "01489", "01496", "01498",
            "01524", "01530", "01535", "01539", "01566",
            "01567", "01569", "01579", "01581", "01584",
            "01596", "01603", "01604", "01607", "01610",
            "01612", "01621", "01623", "01630", "01632",
            "01637", "01641", "01659", "01671", "01681",
            "01684", "01694", "01695", "01699", "01715",
            "01724", "01730", "01739", "01741", "01751",
            "01754", "01763", "01775", "01776", "01808",
            "01812", "01817", "01828", "01831", "01832",
            "01833", "01834", "01846", "01849", "01856",
            "01857", "01861", "01867", "01879", "01883",
            "01888", "01892", "01901", "01906", "01911",
            "01913", "01914", "01916", "01917", "01928",
            "01936", "01939", "01944", "01948", "01949",
            "01958", "01963", "01964", "01967", "01977",
            "01982", "01990", "01993", "01998", "02001",
            "02008", "02009", "02020", "02024", "02025",
            "02028", "02030", "02040", "02041", "02042",
            "02043", "02046", "02053", "02057", "02061",
            "02062", "02069", "02076", "02077", "02078",
            "02087", "02088", "02104", "02105", "02109",
            "02112", "02115", "02130", "02131", "02137",
            "02148", "02151", "02152", "02164", "02171",
            "02172", "02181", "02184", "02189", "02190",
            "02196", "02199", "02200", "02203", "02206",
            "02208", "02217", "02218", "02224", "02230",
            "02236", "02238", "02242", "02245", "02252",
            "02257", "02260", "02265", "02270", "02272",
            "02273", "02277", "02283", "02286", "02289",
            "02304", "02313", "02322", "02324", "02349",
            "02362", "02365", "02369", "02370", "02372",
            "02375", "02384", "02386", "02387", "02391",
            "02394", "02395", "02397", "02403", "02407",
            "02409", "02419", "02439", "02440", "02443",
            "02444", "02445", "02450", "02451", "02475",
            "02478", "02481", "02482", "02490", "02501",
            "02504", "02510", "02511", "02515", "02516",
            "02517", "02523", "02525", "02531", "02535",
            "02536", "02555", "02557", "02559", "02564",
            "02565", "02576", "02583", "02589", "02590",
            "02598", "02615", "02618", "02619", "02626",
            "02630", "02634", "02637", "02641", "02653",
            "02658", "02663", "02667", "02669", "02670",
            "02671", "02674", "02676", "02678", "02687",
            "02715", "02725", "02726", "02730", "02734",
            "02736", "02740", "02743", "02747", "02750",
            "02755", "02758", "02763", "02772", "02777",
            "02780", "02784", "02786", "02791", "02792",
            "02798", "02805", "02809", "02811", "02812",
            "02813", "02833", "02839", "02840", "02844",
            "02848", "02851", "02854", "02860", "02862",
            "02863", "02866", "02869", "02872", "02875",
            "02882", "02893", "02897", "02904", "02907",
            "02910", "02917", "02923", "02935", "02938",
            "02945", "02949", "02950", "02951", "02956",
            "02963", "02964", "02975", "02978", "02981",
            "02993", "02996", "02999", "03005", "03007",
            "03011", "03023", "03025", "03031", "03032",
            "03035", "03043", "03058", "03061", "03068",
            "03069", "03075", "03077", "03080", "03083",
            "03091", "03100", "03104", "03110", "03115",
            "03116", "03125", "03126", "03128", "03145",
            "03146", "03159", "03164", "03176", "03178",
            "03180", "03185", "03191", "03197", "03198",
            "03205", "03206", "03222", "03229", "03233",
            "03235", "03239", "03245", "03251", "03254",
            "03255", "03271", "03273", "03275", "03282",
            "03285", "03293", "03297", "03300", "03307",
            "03311", "03318", "03342", "03346", "03348",
            "03351", "03357", "03363", "03371", "03372",
            "03374", "03375", "03383", "03385", "03397",
            "03398", "03399", "03401", "03405", "03406",
            "03416", "03421", "03422", "03427", "03430",
            "03433", "03435", "03440", "03443", "03445",
            "03464", "03467", "03468", "03473", "03475",
            "03476", "03487", "03496", "03497", "03498",
            "03502", "03504", "03521", "03522", "03523",
            "03526", "03528", "03532", "03542", "03545",
            "03549", "03553", "03558", "03563", "03564",
            "03568", "03573", "03574", "03575", "03579",
            "03581", "03582", "03583", "03587", "03596",
            "03600", "03602", "03604", "03606", "03609",
            "03613", "03626", "03635", "03638", "03640",
            "03641", "03648", "03650", "03653", "03656",
            "03658", "03663", "03665", "03671", "03674",
            "03676", "03678", "03679", "03680", "03683",
            "03695", "03696", "03697", "03701", "03702",
            "03703", "03706", "03711", "03714", "03720",
            "03722", "03724", "03726", "03727", "03728",
            "03735", "03737", "03743", "03751", "03753",
            "03754", "03756", "03764", "03765", "03766",
            "03772", "03778", "03779", "03781", "03785",
            "03790", "03804", "03811", "03819", "03821",
            "03830", "03842", "03848", "03851", "03868",
            "03881", "03883", "03891", "03892", "03895",
            "03896", "03908", "03915", "03925", "03939",
            "03941", "03943", "03949", "03952", "03962",
            "03970", "03971", "03977", "03978", "03980",
            "03981", "03997", "04000", "04006", "04008",
            "04014", "04024", "04034", "04037", "04040",
            "04046", "04047", "04057", "04059", "04066",
            "04069", "04070", "04094", "04105", "04106",
            "04111", "04114", "04120", "04121", "04123",
            "04126", "04132", "04135", "04137", "04147",
            "04158", "04165", "04168", "04177", "04180",
            "04187", "04193", "04205", "04207", "04220",
            "04234", "04235", "04236", "04246", "04247",
            "04249", "04251", "04263", "04265", "04266",
            "04273", "04279", "04287", "04288", "04300",
            "04316", "04333", "04353", "04363", "04366",
            "04371", "04378", "04380", "04387", "04389",
            "04390", "04395", "04402", "04406", "04407",
            "04415", "04418", "04433", "04437", "04449",
            "04476", "04478", "04489", "04491", "04494",
            "04499", "04501", "04506", "04517", "04525",
            "04530", "04531", "04534", "04543", "04551",
            "04553", "04563", "04565", "04577", "04580",
            "04581", "04586", "04591", "04600", "04601",
            "04603", "04605", "04617", "04629", "04630",
            "04631", "04645", "04660", "04664", "04686",
            "04692", "04693", "04711", "04729", "04741",
            "04742", "04766", "04775", "04779", "04785",
            "04801", "04806", "04811", "04851", "04854",
            "04869", "04875", "04876", "04878", "04885",
            "04889", "04901", "04902", "04909", "04919",
            "04969", "04970", "04986", "04995", "04996",
            "04997", "04998", "05000", "05007", "05025",
            "05031", "05033", "05041", "05048", "05055",
            "05060", "05075", "05087", "05105", "05115",
            "05116", "05125", "05151", "05161", "05169",
            "05178", "05179", "05198", "05216", "05218",
            "05244", "05256", "05259", "05269", "05289",
            "05290", "05334", "05352", "05375", "05377",
            "05394", "05401", "05418", "05419", "05422",
            "05427", "05438", "05490", "05504", "05508",
            "05553", "05558", "05564", "05570", "05580",
            "05597", "05614", "05657", "05663", "05720",
            "05770", "05787", "05789", "05816", "05846",
            "05896", "05983", "06156", "06193", "06200",
            "06235", "06303", "06306", "06351", "06424",
            "06430", "06453", "06494", "06656", "06720",
            "06740", "06900", "06986"]

    elif workflow == "Cengage":
        article_blacklist = [
            "00003", "00005", "00007", "00011", "00012", "00013", "00031", "00036", "00047",
            "00048", "00049", "00051", "00065", "00067", "00068", "00070", "00078", "00090",
            "00093", "00102", "00105", "00109", "00116", "00117", "00133", "00160", "00170",
            "00171", "00173", "00178", "00181", "00183", "00184", "00190", "00205", "00218",
            "00220", "00230", "00231", "00240", "00242", "00243", "00247", "00248", "00260",
            "00269", "00270", "00278", "00281", "00286", "00288", "00290", "00291", "00299",
            "00301", "00302", "00306", "00308", "00311", "00312", "00321", "00324", "00326",
            "00327", "00329", "00333", "00334", "00336", "00337", "00340", "00347", "00348",
            "00351", "00352", "00353", "00354", "00358", "00362", "00365", "00367", "00378",
            "00380", "00385", "00386", "00387", "00400", "00411", "00415", "00421", "00422",
            "00425", "00426", "00429", "00435", "00444", "00450", "00452", "00458", "00459",
            "00461", "00467", "00471", "00473", "00475", "00476", "00477", "00481", "00482",
            "00488", "00491", "00498", "00499", "00505", "00508", "00515", "00518", "00522",
            "00523", "00533", "00534", "00537", "00542", "00558", "00563", "00565", "00569",
            "00571", "00572", "00573", "00577", "00590", "00592", "00593", "00594", "00603",
            "00605", "00615", "00625", "00626", "00631", "00632", "00633", "00638", "00639",
            "00640", "00641", "00642", "00646", "00647", "00648", "00654", "00655", "00658",
            "00659", "00662", "00663", "00666", "00668", "00669", "00672", "00675", "00676",
            "00683", "00691", "00692", "00699", "00704", "00708", "00710", "00712", "00723",
            "00726", "00729", "00731", "00736", "00744", "00745", "00747", "00750", "00757",
            "00759", "00762", "00767", "00768", "00772", "00776", "00778", "00780", "00782",
            "00785", "00790", "00791", "00792", "00799", "00800", "00801", "00802", "00804",
            "00806", "00808", "00813", "00822", "00824", "00825", "00828", "00829", "00842",
            "00844", "00845", "00855", "00856", "00857", "00861", "00862", "00863", "00866",
            "00868", "00873", "00882", "00884", "00886", "00895", "00899", "00903", "00905",
            "00914", "00924", "00926", "00932", "00933", "00940", "00943", "00947", "00948",
            "00951", "00953", "00954", "00958", "00960", "00961", "00963", "00966", "00967",
            "00969", "00971", "00983", "00992", "00994", "00996", "00999", "01004", "01008",
            "01009", "01020", "01029", "01030", "01042", "01045", "01061", "01064", "01067",
            "01071", "01074", "01084", "01085", "01086", "01089", "01096", "01098", "01102",
            "01104", "01108", "01114", "01115", "01119", "01120", "01123", "01127", "01133",
            "01135", "01136", "01138", "01139", "01140", "01149", "01157", "01159", "01160",
            "01169", "01179", "01180", "01197", "01201", "01202", "01206", "01211", "01213",
            "01214", "01221", "01222", "01228", "01229", "01233", "01234", "01236", "01239",
            "01252", "01256", "01257", "01267", "01270", "01273", "01279", "01287", "01289",
            "01291", "01293", "01294", "01295", "01296", "01298", "01299", "01305", "01308",
            "01310", "01311", "01312", "01319", "01322", "01323", "01326", "01328", "01339",
            "01340", "01341", "01345", "01350", "01355", "01369", "01370", "01374", "01381",
            "01385", "01386", "01387", "01388", "01402", "01403", "01412", "01414", "01426",
            "01428", "01433", "01434", "01438", "01439", "01440", "01456", "01457", "01460",
            "01462", "01465", "01469", "01473", "01479", "01481", "01482", "01483", "01488",
            "01489", "01494", "01496", "01498", "01501", "01503", "01514", "01515", "01516",
            "01519", "01524", "01530", "01535", "01539", "01541", "01557", "01561", "01566",
            "01567", "01569", "01574", "01579", "01581", "01584", "01587", "01596", "01597",
            "01599", "01603", "01604", "01605", "01607", "01608", "01610", "01612", "01621",
            "01623", "01630", "01632", "01633", "01637", "01641", "01658", "01659", "01662",
            "01663", "01671", "01680", "01681", "01684", "01694", "01695", "01699", "01700",
            "01710", "01715", "01724", "01730", "01738", "01739", "01741", "01749", "01751",
            "01754", "01760", "01763", "01775", "01776", "01779", "01808", "01809", "01812",
            "01816", "01817", "01820", "01828", "01831", "01832", "01833", "01834", "01839",
            "01845", "01846", "01849", "01856", "01857", "01861", "01867", "01873", "01879",
            "01883", "01888", "01892", "01893", "01901", "01906", "01911", "01913", "01914",
            "01916", "01917", "01926", "01928", "01936", "01939", "01944", "01948", "01949",
            "01958", "01963", "01964", "01967", "01968", "01977", "01979", "01982", "01990",
            "01993", "01998", "02001", "02008", "02009", "02020", "02024", "02025", "02028",
            "02030", "02040", "02041", "02042", "02043", "02046", "02053", "02057", "02061",
            "02062", "02069", "02076", "02077", "02078", "02087", "02088", "02094", "02104",
            "02105", "02109", "02112", "02115", "02130", "02131", "02137", "02148", "02151",
            "02152", "02164", "02171", "02172", "02181", "02184", "02189", "02190", "02196",
            "02199", "02200", "02203", "02206", "02208", "02217", "02218", "02224", "02230",
            "02236", "02238", "02242", "02245", "02252", "02257", "02260", "02265", "02270",
            "02272", "02273", "02277", "02283", "02286", "02289", "02304", "02313", "02322",
            "02324", "02349", "02362", "02365", "02369", "02370", "02372", "02375", "02384",
            "02386", "02387", "02391", "02394", "02395", "02397", "02403", "02407", "02409",
            "02419", "02439", "02440", "02443", "02444", "02445", "02450", "02451", "02475",
            "02478", "02481", "02482", "02490", "02501", "02504", "02510", "02511", "02515",
            "02516", "02517", "02523", "02525", "02531", "02535", "02536", "02555", "02557",
            "02559", "02564", "02565", "02576", "02583", "02589", "02590", "02598", "02615",
            "02618", "02619", "02626", "02630", "02634", "02637", "02641", "02653", "02658",
            "02663", "02667", "02669", "02670", "02671", "02674", "02676", "02678", "02687",
            "02715", "02725", "02726", "02730", "02734", "02736", "02740", "02743", "02747",
            "02750", "02755", "02758", "02763", "02772", "02777", "02780", "02784", "02786",
            "02791", "02792", "02798", "02805", "02809", "02811", "02812", "02813", "02833",
            "02839", "02840", "02844", "02848", "02851", "02854", "02860", "02862", "02863",
            "02866", "02869", "02872", "02875", "02882", "02893", "02897", "02904", "02907",
            "02910", "02917", "02923", "02935", "02938", "02945", "02948", "02949", "02950",
            "02951", "02956", "02963", "02964", "02975", "02978", "02981", "02993", "02996",
            "02999", "03005", "03007", "03011", "03023", "03025", "03031", "03032", "03035",
            "03043", "03058", "03061", "03068", "03069", "03075", "03077", "03080", "03083",
            "03091", "03100", "03104", "03110", "03115", "03116", "03125", "03126", "03128",
            "03145", "03146", "03159", "03164", "03176", "03178", "03180", "03185", "03189",
            "03191", "03197", "03198", "03205", "03206", "03222", "03229", "03233", "03235",
            "03239", "03245", "03251", "03254", "03255", "03256", "03270", "03271", "03273",
            "03275", "03282", "03285", "03293", "03297", "03300", "03307", "03311", "03318",
            "03342", "03346", "03348", "03351", "03357", "03363", "03371", "03372", "03374",
            "03375", "03383", "03385", "03397", "03398", "03399", "03401", "03405", "03406",
            "03416", "03421", "03422", "03427", "03430", "03433", "03435", "03440", "03443",
            "03445", "03464", "03467", "03468", "03473", "03475", "03476", "03487", "03496",
            "03497", "03498", "03502", "03504", "03521", "03522", "03523", "03526", "03528",
            "03532", "03542", "03545", "03549", "03553", "03558", "03563", "03564", "03568",
            "03573", "03574", "03575", "03579", "03581", "03582", "03583", "03587", "03596",
            "03600", "03602", "03604", "03606", "03609", "03613", "03614", "03626", "03635",
            "03638", "03640", "03641", "03648", "03650", "03653", "03656", "03658", "03663",
            "03665", "03671", "03674", "03676", "03678", "03679", "03680", "03683", "03695",
            "03696", "03697", "03701", "03702", "03703", "03706", "03711", "03714", "03720",
            "03722", "03724", "03726", "03727", "03728", "03735", "03737", "03743", "03751",
            "03753", "03754", "03756", "03764", "03765", "03766", "03772", "03778", "03779",
            "03781", "03785", "03790", "03804", "03811", "03819", "03821", "03830", "03842",
            "03848", "03851", "03868", "03881", "03883", "03891", "03892", "03895", "03896",
            "03908", "03915", "03925", "03939", "03941", "03943", "03949", "03952", "03962",
            "03970", "03971", "03977", "03978", "03980", "03981", "03997", "04000", "04006",
            "04008", "04014", "04024", "04034", "04037", "04040", "04046", "04047", "04052",
            "04057", "04059", "04066", "04069", "04070", "04094", "04105", "04106", "04111",
            "04114", "04120", "04121", "04123", "04126", "04132", "04135", "04137", "04147",
            "04158", "04165", "04168", "04177", "04180", "04186", "04187", "04193", "04205",
            "04207", "04220", "04232", "04234", "04235", "04236", "04246", "04247", "04249",
            "04251", "04260", "04263", "04265", "04266", "04273", "04279", "04287", "04288",
            "04300", "04316", "04333", "04346", "04353", "04363", "04366", "04371", "04378",
            "04379", "04380", "04387", "04389", "04390", "04395", "04402", "04406", "04407",
            "04415", "04418", "04433", "04437", "04449", "04463", "04476", "04478", "04489",
            "04490", "04491", "04494", "04499", "04501", "04506", "04517", "04525", "04530",
            "04531", "04534", "04535", "04543", "04550", "04551", "04553", "04563", "04565",
            "04577", "04580", "04581", "04585", "04586", "04591", "04599", "04600", "04601",
            "04603", "04605", "04617", "04629", "04630", "04631", "04634", "04645", "04660",
            "04664", "04686", "04692", "04693", "04711", "04726", "04729", "04741", "04742",
            "04766", "04775", "04779", "04785", "04790", "04801", "04803", "04806", "04811",
            "04837", "04851", "04854", "04869", "04871", "04872", "04875", "04876", "04878",
            "04883", "04885", "04889", "04901", "04902", "04909", "04919", "04940", "04953",
            "04960", "04969", "04970", "04979", "04986", "04995", "04996", "04997", "04998",
            "05000", "05003", "05007", "05025", "05031", "05033", "05041", "05042", "05048",
            "05055", "05060", "05075", "05087", "05098", "05105", "05115", "05116", "05118",
            "05125", "05151", "05154", "05161", "05165", "05166", "05169", "05178", "05179",
            "05198", "05216", "05218", "05224", "05242", "05244", "05256", "05259", "05269",
            "05279", "05289", "05290", "05291", "05334", "05338", "05352", "05375", "05377",
            "05378", "05394", "05401", "05413", "05418", "05419", "05421", "05422", "05423",
            "05427", "05438", "05447", "05449", "05457", "05463", "05464", "05472", "05477",
            "05490", "05491", "05503", "05504", "05508", "05534", "05544", "05553", "05557",
            "05558", "05560", "05564", "05570", "05580", "05597", "05604", "05606", "05608",
            "05614", "05635", "05657", "05663", "05701", "05720", "05733", "05770", "05787",
            "05789", "05808", "05816", "05826", "05835", "05846", "05849", "05861", "05868",
            "05871", "05875", "05896", "05899", "05959", "05983", "06003", "06024", "06034",
            "06054", "06068", "06074", "06100", "06132", "06156", "06166", "06179", "06184",
            "06193", "06200", "06235", "06250", "06303", "06306", "06346", "06351", "06369",
            "06380", "06400", "06412", "06424", "06430", "06453", "06494", "06536", "06557",
            "06565", "06633", "06656", "06717", "06720", "06740", "06758", "06782", "06808",
            "06837", "06877", "06883", "06900", "06956", "06986", "06995", "07074", "07083",
            "07108", "07157", "07204", "07239", "07322", "07364", "07390", "07431", "07482",
            "07527", "07532", "07586", "07604"
        ]
    elif workflow == "GoOA":
        article_blacklist = []

    else:
        article_blacklist = []

    return article_blacklist
