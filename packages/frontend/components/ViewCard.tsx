import React from 'react';
import { Box, Text, Image, Stack, HStack, Flex, Center } from "@chakra-ui/react";

type ViewCardProps = {
    imageTestId: string;
    textTestId: string;
    onClick: () => void;
};

const ViewCard: React.FC<ViewCardProps> = ({ imageTestId, textTestId, onClick }) => (
    <Box
        onClick={onClick}
        style={{
            cursor: 'pointer',  // Change cursor to pointer on hover
            backgroundColor: 'rgba(255, 255, 255, 0.28)',
            backdropFilter: 'blur(10px)',
            boxShadow: '0px 0px 10px rgba(255, 105, 180, 0.5)'
        }}
        maxW='sm'
        borderWidth='1px'
        borderRadius='lg'
        overflow='hidden'
        minW='sm'
        maxH='lg'
        minH='450px'
    >
        <Center>
            <Box paddingTop="20px">
                <Image
                    data-testid={imageTestId}
                    src='images/amex_platinum.png'
                    borderRadius='lg'
                />
            </Box>
        </Center>
        <Stack mt='6' spacing='3' p='4' marginLeft='20px' marginRight='20px'>
            <HStack>
                <Text
                    data-testid={textTestId}
                    bgGradient='linear(to-t, #5200FF, #FF8A00)'
                    bgClip='text'
                    fontFamily="Outfit"
                    fontWeight="600"
                    fontSize="30px"
                >
                    #1
                </Text>
                <Text
                    fontFamily="Outfit"
                    fontWeight="600"
                    fontSize="30px"
                    textColor="#FFFFFF"
                >
                    Amex Platinum
                </Text>
            </HStack>
            <Text
                fontFamily="Outfit"
                fontWeight="400"
                fontSize="15px"
                textColor="#FFFFFF"
            >
                - Cool Text
            </Text>
        </Stack>
        <Flex
            justify='center' // Center horizontally
            align='center'  // Center vertically
            direction='column' // Stack children vertically
            height="50px" // Set the height of the container
            marginTop="20px"
        >
            <Box
                as='button'
                color='white'
                fontWeight='bold'
                borderRadius='12px'
                width="85%"
                height="50px"
                bgGradient='linear(to-l, #5200FF,#FF0080, #FF8A00)'
            >
                <Text>Start Now</Text>
            </Box>
        </Flex>
    </Box>
);

export default ViewCard;
