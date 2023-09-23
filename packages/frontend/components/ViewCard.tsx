import React from 'react';
import { Box, Button, Divider, Heading, Stack, Text, Image } from '@chakra-ui/react';

const ViewCard = () => (
  <Box backgroundColor="#FFFFFF" maxW='sm' borderWidth='1px' borderRadius='lg' overflow='hidden' minW='sm' maxH='lg' minH='450px'>
    <Image
      src='images/amex_gold.png'
      borderRadius='lg'
    />
    <Stack mt='6' spacing='3' p='4'>
      <Heading size='md'>Living room Sofa</Heading>
      <Text>
        Cool Text
      </Text>
      <Text color='blue.600' fontSize='2xl'>
        $450
      </Text>
    </Stack>
    <Divider />
      <Button variant='solid' colorScheme='blue'>
        Buy now
      </Button>
  </Box>
);

export default ViewCard;
