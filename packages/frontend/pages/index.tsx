import type { NextPage } from "next";
import { Box, Heading, HStack, VStack, Image, Text } from "@chakra-ui/react";
import Head from "next/head";
import React, { useState, useCallback, useEffect } from "react";
import { useRouter } from "next/router";
import { usePlaidLink } from "react-plaid-link";
import PageLayout from "../components/Layout/PageLayout";
import GradientSpotlight from "../components/GradientSpotlight";

async function fetchTransactions() {
  try {
    const response = await fetch("/api/get-transactions", {
      method: "POST",
      headers: {
        Authorization: window.localStorage.getItem("token"),
      },
    }); // Use the correct API endpoint
    if (!response.ok) {
      throw new Error("Failed to fetch transactions");
    }
    const transactionsData = await response.json();
    // Process and display the transactionsData as needed
    console.log(transactionsData); // You can replace this with your logic to display the data
  } catch (error) {
    console.error("Error fetching transactions:", error);
  }
}

export default function PlaidLink() {
  const router = useRouter();
  const [token, setToken] = useState(null);

  useEffect(() => {
    const createLinkToken = async () => {
      const response = await fetch("/api/create-link-token", {
        method: "POST",
      });
      if (!response.ok) {
        throw new Error("Failed to create link token");
      }

      const { link_token } = await response.json();
      setToken(link_token);
    };
    createLinkToken();
    fetchTransactions();
  }, []);

  const onSuccess = useCallback(async (publicToken) => {
    const res = await fetch("/api/exchange-public-token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ public_token: publicToken }),
    });
    const token = await res.json();
    window.localStorage.setItem("token", token.token);
    console.log(token);
    router.push("/main-page");
  }, []);

  const { open, ready } = usePlaidLink({
    token,
    onSuccess,
  });
  // const handleButtonClick = () => {
  //   // Use the router to navigate to a different page
  //   router.push("main-page"); // Replace with the actual path
  // };

  return (
    <Box backgroundColor={"#06021C"}>
      <PageLayout title={"cardforme"}>
        <HStack spacing={0} w={"100%"} h={"100%"}>
          <Box width={"50%"} height={"100vh"}>
            <HStack paddingLeft={10} paddingTop={10} spacing={-1.75}>
              <Text
                fontFamily={"Monoton"}
                fontWeight={"400"}
                fontSize={"65px"}
                lineHeight={"110%"}
                color={"#FF8A00"}
                textShadow={"0px 4px 4px rgba(0, 0, 0, 0.25)"}
              >
                c
              </Text>
              <Text
                fontFamily={"Monoton"}
                fontWeight={"400"}
                fontSize={"65px"}
                lineHeight={"110%"}
                color={"#FF00C7"}
                textShadow={"0px 4px 4px rgba(0, 0, 0, 0.25)"}
              >
                m
              </Text>
            </HStack>
            <VStack align={"left"} paddingLeft={"10"} paddingTop={"40"}>
              <Text
                fontFamily={"Outfit"}
                fontWeight={"600"}
                fontSize={"100px"}
                lineHeight={"90%"}
                textColor={"#FFFFFF"}
              >
                find the
              </Text>
              <Text
                fontFamily={"Outfit"}
                fontWeight={"600"}
                fontSize={"100px"}
                lineHeight={"90%"}
                textColor={"#FFFFFF"}
              >
                card for
              </Text>
              <Text
                bgGradient={
                  "linear(to-l, #5200FF,#5200FF, #5200FF,#FF0080, #FF8A00)"
                }
                bgClip={"text"}
                fontFamily={"Outfit"}
                fontWeight={"600"}
                fontSize={"100px"}
                lineHeight={"90%"}
                paddingBottom={"100px"}
              >
                you
              </Text>
              <Box
                as={"button"}
                color={"white"}
                fontWeight={"bold"}
                borderRadius={"12px"}
                width={"200px"}
                height={"50px"}
                bgGradient={"linear(to-l, #5200FF,#FF0080, #FF8A00)"}
                marginTop={"50px"}
                zIndex={1}
                _hover={{
                  // make it slightly bigger and glow
                  transform: "scale(1.02)",
                }}
                onClick={() => open()}
              >
                <Text>Start Now</Text>
              </Box>
              {/* <Box */}
              {/*  as={"button"} */}
              {/*  color={"white"} */}
              {/*  fontWeight={"bold"} */}
              {/*  borderRadius={"12px"} */}
              {/*  width={"200px"} */}
              {/*  height={"50px"} */}
              {/*  bgGradient={"linear(to-l, #5200FF,#FF0080, #FF8A00)"} */}
              {/*  marginTop={"50px"} */}
              {/*  zIndex={1} */}
              {/*  _hover={{ */}
              {/*    transform: "scale(1.02)", */}
              {/*  }} */}
              {/*  onClick={fetchTransactions} // Call the fetchTransactions function when the button is clicked */}
              {/* > */}
              {/*  <Text>Fetch Transactions</Text> */}
              {/* </Box> */}
            </VStack>
          </Box>
          <Box
            position={"absolute"}
            top={"40"}
            left={"-30"}
            width={"100%"}
            height={"100%"}
          >
            <GradientSpotlight />
          </Box>

          <Box width={"50%"} height={"100vh"}>
            <Box
              style={{
                width: "100%",
                height: "100%",
                background:
                  "conic-gradient(from 90deg at 0.00% 100.00%, #5200FF 180deg, #FF8A00 360deg)",
              }}
            >
              <Box />
            </Box>
            <Image
              src={"images/discover_floating.png"}
              position={"absolute"}
              top={"460"}
              left={"680"}
              width={"40%"}
              height={"40%"}
            />
            <Image
              src={"images/floating_cards.png"}
              position={"absolute"}
              top={"70"}
              left={"650"}
              width={"60%"}
              height={"60%"}
            />
          </Box>
        </HStack>
      </PageLayout>
    </Box>
  );
}
