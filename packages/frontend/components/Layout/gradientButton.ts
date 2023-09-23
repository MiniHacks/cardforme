// give me a ts file which will be a react button component for later use using chakraui

import { Button } from '@chakra-ui/react';
import React from 'react';

interface Props {
  children: string;
}

import { Button, ButtonProps } from '@chakra-ui/react';
import React from 'react';

interface Props extends ButtonProps {
    children: string;
}

const GradientButton: React.FC<Props> = ({ children, ...rest }) => {
    return (
        <Button
            colorScheme="blue"
            variant="solid"
            w="100%"
            h="50px"
            borderRadius="10px"
            boxShadow="0px 4px 4px rgba(0, 0, 0, 0.25)"
            bgGradient="linear(to-r, #FF6B6B, #FF8E53)"
            {...rest}
        >
            {children}
        </Button>
    );
};

export default GradientButton;



