import Head from "next/head";

const DEFAULT_TITLE = "MiniHacks Presents:";
const DEFAULT_DESC = "A Hackathon Project!";

export type MyHeadingProps = {
  title?: string;
};

const MyHeading = ({ title }: MyHeadingProps): JSX.Element => (
  <Head>
    <title>{title || DEFAULT_TITLE}</title>
    <meta name={"description"} content={DEFAULT_DESC} />
    <link rel={"icon"} href={"/favicon.ico"} />
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Monoton&family=Outfit&display=swap');
    </style>
  </Head>
);
export default MyHeading;
