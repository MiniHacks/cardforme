import { ColorModeScript } from "@chakra-ui/react";
import { Head, Html, Main, NextScript } from "next/document";
import theme from "../theme";

export default function Document(): JSX.Element {
  return (
    <Html lang={"en"}>
      <Head>
        <title>Connect a bank</title>
        <script
          src={"https://cdn.plaid.com/link/v2/stable/link-initialize.js"}
        />
        <link rel={"preconnect"} href={"https://fonts.googleapis.com"} />
        <link rel={"preconnect"} href={"https://fonts.gstatic.com"} />
        <link
          href={
            "https://fonts.googleapis.com/css2?family=Monoton&family=Outfit:wght@100;200;300;400;500;600;700;800;900&display=swap"
          }
          rel={"stylesheet"}
        />
      </Head>
      <body>
        <ColorModeScript initialColorMode={theme.config.initialColorMode} />
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
