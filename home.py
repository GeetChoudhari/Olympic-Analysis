import streamlit as st


def home():
    header = st.container()
    explain = st.container()

    with header:
        st.markdown("<h1 style='text-align: center; color:Red ;'>Olympics Games</h1>",
                    unsafe_allow_html=True)

    with explain:
        st.title("History of Olympics Games")
        st.write("Olympic Games or Olympics are leading international sporting events featuring summer and winter sports competitions in which thousands of athletes from around the world participate in a variety of competitions. The Olympic Games are considered the world's foremost sports competition with more than 200 nations participating. The Olympic Games are normally held every four years, alternating between the Summer and Winter Olympics every two years in the four-year period.")
        path = "D:\Olympics Data\images\Olympic_rings_without_rims.svg.png"
        st.write("The Summer Olympic Games, also known as the Games of the Olympiad, are a major international multi-sport event normally held once every four years. The inaugural Games took place in 1896 in Athens, Greece. The International Olympic Committee (IOC) organises the Games and oversees the host city's preparations. In each Olympic event, gold medals are awarded for first place, silver medals are awarded for second place, and bronze medals are awarded for third place; this tradition began in 1904. The Winter Olympic Games were created out of the success of the Summer Olympics. It is regarded as the largest and most prestigious multi-sport international event in the world.")
        st.write("\nThe Olympics have increased in scope from a 42-event competition programme with fewer than 250 male competitors from 14 nations in 1896 to 306 events with 11,238 competitors (6,179 men, 5,059 women) from 206 nations in 2016. The Summer Olympics have been hosted on five continents by a total of nineteen countries. The Games have been held four times in the United States (1904, 1932, 1984, and 1996), three times in Great Britain (1908, 1948, and 2012), twice each in Greece (1896 and 2004), France (1900 and 1924), Germany (1936 and 1972), Australia (1956 and 2000), and Japan (1964 and 2020) and once each in Sweden (1912), Belgium (1920), Netherlands (1928), Finland (1952), Italy (1960), Mexico (1968), Canada (1976), Soviet Union (1980), South Korea (1988), Spain (1992), China (2008), and Brazil (2016).")
        st.write(
            "The Winter Olympic Games (French: Jeux olympiques d'hiver)[nb 1] is a major international multi-sport event held once every four years for sports practiced on snow and ice. The first Winter Olympic Games, the 1924 Winter Olympics, were held in Chamonix, France.")
        st.write("\nThe Winter Olympic Games have been hosted on three continents by twelve countries. They have been held four times in the United States (1932, 1960, 1980, and 2002), three times in France (1924, 1968, and 1992) and twice each in Austria (1964 and 1976), Canada (1988 and 2010), Japan (1972 and 1998), Italy (1956 and 2006), Norway (1952 and 1994) and Switzerland (1928 and 1948). Also, the Winter Olympic Games have been held just once each in Germany (1936), Yugoslavia (1984), Russia (2014).To date, twelve countries have participated in every Winter Olympic Games – Austria, Canada, Finland, France, Great Britain, Hungary, Italy, Norway, Poland, Sweden, Switzerland and the United States. Six of these countries have won medals at every Winter Olympic Games – Austria, Canada, Finland, Norway, Sweden, and the United States. The only country to have won a gold medal at every Winter Olympic Games is the United States. Norway leads the all-time Olympic Games medal table for Winter Olympic Games. When including defunct states, Germany (including the former countries of West Germany and East Germany) leads, followed by Norway, Russia (including the former Soviet Union), and the United States.")
        st.write("\n Thanks to CampusX")
