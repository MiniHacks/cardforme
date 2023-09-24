import React from 'react';
import { Box, Text, Image, Stack, HStack, Flex, Center } from "@chakra-ui/react";

type ViewCardProps = {
  imageSrc: string;
  cardName: string;
  cardDescription: string;
  onClick: () => void;
  cardNumber: number;
};

const ViewCard: React.FC<ViewCardProps> = ({
                                             imageSrc,
                                             cardName,
                                             cardDescription,
                                             onClick,
                                             cardNumber,
                                           }) => (
  <Box
    onClick={onClick}
    style={{
      cursor: 'pointer',
      backgroundColor: 'rgba(255, 255, 255, 0.10)',
      backdropFilter: 'blur(10px)',
      boxShadow: '0px 0px 0px rgba(255, 105, 180, 1)',
      transition: 'transform 0.3s', // Add transition for smooth scaling
    }}
    maxW='sm'
    borderRadius='lg'
    overflow='hidden'
    minW='sm'
    maxH='500px'
    minH='500px'
    _hover={{ transform: 'scale(1.02)' }} // Apply the scale effect on hover
  >
    <Center>
      <Box paddingTop="20px">
        <Image
          src={imageSrc}
          borderRadius='lg'
          maxW='100%'
          maxH='100%'
        />
      </Box>
    </Center>
    <Stack mt='6' spacing='3' p='4' marginLeft='20px' marginRight='20px'>
      <HStack>
        <Text
          bgGradient='linear(to-t, #5200FF, #FF8A00)'
          bgClip='text'
          fontFamily="Outfit"
          fontWeight="600"
          fontSize="30px"
        >
          #{cardNumber}
        </Text>
        <Text
          fontFamily="Outfit"
          fontWeight="600"
          fontSize="30px"
          textColor="#FFFFFF"
        >
          {cardName}
        </Text>
      </HStack>
      <Text
        fontFamily="Outfit"
        fontWeight="400"
        fontSize="15px"
        textColor="#FFFFFF"
      >
        {cardDescription}
      </Text>
    </Stack>
    <Flex
      justify='center'
      align='center'
      direction='column'
      height="50px"
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
        _hover={{
          transform: 'scale(1.02)',
        }}
      >
        <Text>Start Now</Text>
      </Box>
    </Flex>
  </Box>
);

export default ViewCard;
