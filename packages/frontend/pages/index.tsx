import type { NextPage } from "next";
import { Box, Heading, HStack, VStack, Image, Text } from "@chakra-ui/react";
import Head from "next/head";
import React, { useState, useCallback, useEffect } from "react";
import { useRouter } from "next/router";
import { usePlaidLink } from "react-plaid-link";
import { Background } from "../components/Background";
import PageLayout from "../components/Layout/PageLayout";

export default function PlaidLink() {
  const [token, setToken] = useState(null);

  useEffect(() => {
    const createLinkToken = async () => {
      const response = await fetch("/api/create-link-token", {
        method: "POST",
      });
      const { link_token } = await response.json();
      setToken(link_token);
    };
    createLinkToken();
  }, []);

  const onSuccess = useCallback(async (publicToken) => {
    await fetch("/api/exchange-public-token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ public_token: publicToken }),
    });
    Router.push("/dashboard");
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
        <HStack spacing={0} w={"100%"}>
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
                fontWeight={"700"}
                fontSize={"100px"}
                lineHeight={"90%"}
                textColor={"#FFFFFF"}
              >
                find the
              </Text>
              <Text
                fontFamily={"Outfit"}
                fontWeight={"700"}
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
                fontWeight={"900"}
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
                _hover={{
                  // make it slightly bigger and glow
                  transform: "scale(1.01)",
                  boxShadow: "0 0 4px #FFF",
                }}
                onClick={() => open()}
              >
                <Text>Start Now</Text>
              </Box>
            </VStack>
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
              top={"520"}
              left={"700"}
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
