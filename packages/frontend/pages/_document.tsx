import { ColorModeScript } from "@chakra-ui/react";
import { Head, Html, Main, NextScript } from "next/document";
import theme from "../theme";

export default function Document(): JSX.Element {
  return (
    <Html lang={"en"}>
        <Head>
            <title>Connect a bank</title>
            <script src="https://cdn.plaid.com/link/v2/stable/link-initialize.js"></script>
        </Head>
        <body>
        <ColorModeScript initialColorMode={theme.config.initialColorMode} />
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
