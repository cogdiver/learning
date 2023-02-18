import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
// import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import hasuras from '@site/static/img/hasuras.png';
import VersionedLink from '@site/src/components/VersionedLink';
import styles from './index.module.scss';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.links}>

          <VersionedLink
            className="button button--primary button--lg"
            to="/cogdiver/back-fastapi/index">
            Backend with Fastapi
          </VersionedLink>
          <VersionedLink
            className="button button--success button--lg"
            to="/cogdiver/data-scala/index">
            Data Management with Scala
          </VersionedLink>
          <VersionedLink
            className="button button--primary button--lg"
            to="/cogdiver/back-go/index">
            Backend with Golang
          </VersionedLink>
        </div>

        {/* <div className={styles.links}>
          <Link
            className="button button--secondary button--lg"
            to="/wiki/">
            Docs Wiki
          </Link>
        </div> */}

        <img src={hasuras} alt="Hasuras Image" />
      </div>
    </header>
  );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout >
      <HomepageHeader />
    </Layout>
  );
}
