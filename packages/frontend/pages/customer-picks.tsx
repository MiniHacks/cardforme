// Home.js
import type { NextPage } from "next";
import { Box, Flex, Heading } from "@chakra-ui/react";
import React from "react";
import ViewCard from "../components/ViewCard";
import GradientSpotlight from "../components/GradientSpotlight";

const Home: NextPage = () => {
  const cardsData = [
    {
      imageSrc: "/images/amex_platinum.png",
      cardName: "Amex Platinum",
      cardDescription: "Travel & Hotel credit",
      link: "https://www.americanexpress.com/us/credit-cards/card/platinum/",
    },
    {
      imageSrc: "/images/chase_sapphire_reserve.png",
      cardName: "Sapphire Reserve",
      cardDescription: "Travel & Hotel credit",
      link: "https://creditcards.chase.com/rewards-credit-cards/sapphire/reserve",
    },
    {
      imageSrc: "/images/discover_it_cash_back.png",
      cardName: "Discover It - CB",
      cardDescription: "Cash back credit",
      link: "https://creditcards.chase.com/cash-back-credit-cards/freedom/unlimited",
    },
  ];

  const cardsPerSlide = 3;
  const [currentIndex, setCurrentIndex] = React.useState(0);

  const handleNext = () => {
    setCurrentIndex(
      (prevIndex) => (prevIndex + cardsPerSlide) % cardsData.length
    );
  };

  const handlePrevious = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === 0
        ? cardsData.length - (cardsData.length % cardsPerSlide)
        : prevIndex - cardsPerSlide
    );
  };

  const pageStyle: React.CSSProperties = {
    backgroundColor: "#06021C",
    height: "100vh",
  };

  const carouselStyle: React.CSSProperties = {
    width: "100%",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    position: "relative",
  };

  const isLastPage = currentIndex + cardsPerSlide >= cardsData.length;

  return (
    <div style={pageStyle}>
      <Box>
        <Heading
          color={"#FFFFFF"}
          fontFamily={"Outfit"}
          ml={192}
          pt={25}
          pb={15}
        >
          Customer Favorites
        </Heading>
      </Box>
      <Box style={carouselStyle}>
        <Box position={"absolute"} left={"-80px"} top={"100px"}>
          <GradientSpotlight /> {/* Use the GradientSpotlight component */}
        </Box>
        <Box position={"absolute"} left={"400px"} top={"0px"}>
          <GradientSpotlight /> {/* Use the GradientSpotlight component */}
        </Box>
        <Box position={"absolute"} left={"1000px"} top={"-200px"} deg={"180px"}>
          <GradientSpotlight /> {/* Use the GradientSpotlight component */}
        </Box>
        <Flex>
          {cardsData
            .slice(currentIndex, currentIndex + cardsPerSlide)
            .map((card, index) => (
              <Box
                zIndex={1}
                key={index}
                marginRight={"20px"} // Add margin between cards
              >
                <ViewCard
                  imageSrc={card.imageSrc}
                  cardName={card.cardName}
                  cardDescription={card.cardDescription}
                  cardNumber={currentIndex + index + 1}
                  onClick={() =>
                    typeof window !== "undefined" && window.open(card.link)
                  }
                />
              </Box>
            ))}
        </Flex>
        {/* Add Next and Previous buttons here */}
      </Box>
    </div>
  );
};

export default Home;
