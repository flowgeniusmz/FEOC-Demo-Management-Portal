import streamlit as st

def benefits_container_intro():
    benefits_container = st.container()
    with benefits_container:
        st.markdown("#### Key Benefits")
        benefits_container_sub1 = st.container()
        with benefits_container_sub1:
            cc_benefits1 = st.columns(4)
            with cc_benefits1[0]:
                benefits_exp1 = st.expander("Alignment of Incentives", expanded=True)
                with benefits_exp1:
                    st.markdown("**Alignment of Incentives**")
                    st.markdown("FEOCs establish a direct link between large emitters (like refineries), emission offset providers (such as CCS projects), and net-zero fuel and product purchasers (like airlines). This alignment of incentives ensures that all parties are vested in the success of emission reduction projects.  Once the FEOCs are activated as electronic contracts binding the parties, the emitters receive the offsets (i.e., before the emission offset projects are operational).")
            with cc_benefits1[1]:
                benefits_exp2 = st.expander("Real Time Tracking and Transparency", expanded=True)
                with benefits_exp2:
                    st.markdown("#### Real Time Tracking and Transparency")
                    st.markdown("FEOCs act as both electronic real-time contracts and transaction ledgers. They provide a fail-safe system for monitoring, validating, and verifying contractual obligations, ensuring absolute transparency and reporting. This real-time tracking enhances trust among parties and allows immediate corrective actions if obligations are unmet.")
            with cc_benefits1[2]:
                benefits_exp3 = st.expander("Cost Recovery for Emitters", expanded=True)
                with benefits_exp3:
                    st.markdown("#### Cost Recovery for Emitters")
                    st.markdown("Refineries investing in CCS projects receive offsets in exchange for their investments. These offsets allow them to forward-sell net-zero fuel to airlines at above-market prices, ensuring the recovery of their capital investment in the CCS project. This cost recovery mechanism is more direct and reliable than traditional project financing methods.")
            with cc_benefits1[3]:
                benefits_exp4 = st.expander("Better Financing Terms for CCS Projects", expanded=True)
                with benefits_exp4:
                    st.markdown("#### Better Financing Terms for CCS Projects")
                    st.markdown("CCS projects benefit from FEOCs by receiving investment capital from emitters, allowing them to develop emission offsets. These 1:1 offsets provide a more secure and attractive funding source than conventional debt and equity project finance strategies. This accelerates project development and supports carbon capture initiatives with large emitters, promoting 'additionality.'")
        benefits_container_sub2 = st.container()
        with benefits_container_sub2:
            cc_benefits2 = st.columns(3)
            with cc_benefits2[0]:
                benefits_exp5 = st.expander("Progress Toward Net-Zero Commitments", expanded=True)
                with benefits_exp5:
                    st.markdown("#### Progress Toward Net-Zero Commitments")
                    st.markdown("Airlines purchasing net-zero fuel can significantly progress toward their net-zero emissions commitments. They can offer net-zero flights at premium prices to recoup the cost of the forward-purchased fuel, aligning with shareholder and customer expectations for responsible operations and potentially boosting their stock prices.")
            with cc_benefits2[1]:
                benefits_exp6 = st.expander("Regulatory and Sustainability Alignment", expanded=True)
                with benefits_exp6:
                    st.markdown("#### Regulatory and Sustainability Alignment")
                    st.markdown("Emitters using FEOCs reduce their carbon footprint and align with regulatory requirements and sustainability goals. This alignment is essential in a world where environmental regulations are becoming stricter, and sustainability is a key consideration for businesses.")
            with cc_benefits2[2]:
                benefits_exp7 = st.expander("FEOC Issuer and Manager Benefits", expanded=True)
                with benefits_exp7:
                    st.markdown("#### FEOC Issuer and Manager Benefits")
                    st.markdown("As the issuer and manager of FEOCs, Faulkner plays a critical role in ensuring the system's integrity by conducting stringent electronic verification and validation in real-time, safeguarding transaction obligations between emitters and CCS projects. This assurance mechanism enhances trust and confidence among all parties involved.")


def benefits_container_website():
    benefits_container = st.container()
    with benefits_container:
        st.markdown("#### Key Benefits")
        benefits_container_sub1 = st.container()
        with benefits_container_sub1:
            st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">""",unsafe_allow_html=True)
            cc_benefits1 = st.columns(4)
            with cc_benefits1[0]:
                st.markdown("""**Real-Time Data Analysis** <i class="fas fa-clock" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                benefits_exp1 = st.expander("Details", expanded=True)
                with benefits_exp1:
                    st.markdown("""Data is captured instantaneously and provided directly to our proprietary AI for interpretation, calculations, verification, and validation.""")
            with cc_benefits1[1]:
                st.markdown("""**Complete Visual Transparency** <i class="fab fa-sistrix" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                benefits_exp2 = st.expander("Details", expanded=True)
                with benefits_exp2:
                    st.markdown("The Certificate is underpinned by every data point, tracing back to its source, capturing the full spectrum of interactions, activity, and calculations.")
            with cc_benefits1[2]:
                st.markdown("""**Data Science Team Oversight** <i class="fas fa-chart-bar" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                benefits_exp3 = st.expander("Details", expanded=True)
                with benefits_exp3:
                    st.markdown("Hands-on approach ensures the certificate is not only data-driven, but also insights-driven, powered by a team that understands the nuances of the data.")
            with cc_benefits1[3]:
                st.markdown("""**Multi-Party Engagement** <i class="fas fa-handshake" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                benefits_exp4 = st.expander("Details", expanded=True)
                with benefits_exp4:
                    st.markdown("Stakeholders operate from a common, unbiased fact base to foster a cohesive, collaborative environment driven from transparency of the FEOC.")
        benefits_container_sub2 = st.container()
        with benefits_container_sub2:
            cc_benefits2 = st.columns(4)
            with cc_benefits2[0]:
                st.markdown("""**AAA-Rated Credit Enhancement** <i class="fas fa-money-bill" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                benefits_exp5 = st.expander("Details", expanded=True)
                with benefits_exp5:
                    st.markdown("Unique guarantee of both principal and interest returns, backed by AAA-rated credit through real-time financial models using historical, engagement, and macroeconomic data.")
            with cc_benefits2[1]:
                st.markdown("""**Fully Tradable Certificates** <i class="fas fa-exchange-alt" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                benefits_exp6 = st.expander("Details", expanded=True)
                with benefits_exp6:
                    st.markdown("Designed to be fully vested upon issuance, transferable, and not subject to recapture, accommodating long-term contracts and investment-grade credit ratings.")
            with cc_benefits2[2]:
                st.markdown("""**Full Investment Lifecycle** <i class="fas fa-sync-alt" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                benefits_exp7 = st.expander("Details", expanded=True)
                with benefits_exp7:
                    st.markdown("Comprehensive range of financial activities not usually bundled in one instrument, streamlined using AI and prompt engineering techniques to minimize human error and maximize data points.")
            with cc_benefits2[3]:
                st.markdown("""**Regulatory Alignment** <i class="fas fa-clipboard-check" style="color: #442c5c;"></i>""", unsafe_allow_html=True)
                benefits_exp8 = st.expander("Details", expanded=True)
                with benefits_exp8:
                    st.markdown("The system autonomously adapts to multiple regulatory frameworks, ensuring that the moment a regulation changes, the system adjusts, maintaining real-time compliance verification.")
