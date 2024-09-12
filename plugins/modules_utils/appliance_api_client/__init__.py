# coding: utf-8

# flake8: noqa

"""
    Appliance Management API

    Management API for the Anapaya EDGE, CORE and GATE appliances

    The version of the OpenAPI document: 0.1.0
    Contact: ops@anapaya.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.config_api import ConfigApi
from openapi_client.api.cppki_api import CppkiApi
from openapi_client.api.debug_api import DebugApi
from openapi_client.api.firewall_api import FirewallApi
from openapi_client.api.health_api import HealthApi
from openapi_client.api.init_api import InitApi
from openapi_client.api.migrations_api import MigrationsApi
from openapi_client.api.network_api import NetworkApi
from openapi_client.api.software_api import SoftwareApi
from openapi_client.api.software_license_api import SoftwareLicenseApi
from openapi_client.api.software_signatures_api import SoftwareSignaturesApi
from openapi_client.api.tools_api import ToolsApi
from openapi_client.api.vpp_api import VppApi
from openapi_client.api.vpp_trace_api import VppTraceApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.accept_filter_matches_prefix import AcceptFilterMatchesPrefix
from openapi_client.models.accept_filter_matches_prefix_data import AcceptFilterMatchesPrefixData
from openapi_client.models.accept_filter_matches_prefix_wrapped import AcceptFilterMatchesPrefixWrapped
from openapi_client.models.announce_filter_matches_prefix import AnnounceFilterMatchesPrefix
from openapi_client.models.announce_filter_matches_prefix_data import AnnounceFilterMatchesPrefixData
from openapi_client.models.announce_filter_matches_prefix_wrapped import AnnounceFilterMatchesPrefixWrapped
from openapi_client.models.any_domain_has_healthy_remote_gateways import AnyDomainHasHealthyRemoteGateways
from openapi_client.models.any_domain_has_healthy_remote_gateways_wrapped import AnyDomainHasHealthyRemoteGatewaysWrapped
from openapi_client.models.appliance_description import ApplianceDescription
from openapi_client.models.bgp_config import BGPConfig
from openapi_client.models.bgp_neighbor import BGPNeighbor
from openapi_client.models.bgp_neighbor_status import BGPNeighborStatus
from openapi_client.models.bgp_neighbors_response_json import BGPNeighborsResponseJson
from openapi_client.models.bgp_response_json import BGPResponseJson
from openapi_client.models.bgp_timers import BGPTimers
from openapi_client.models.base_health_check import BaseHealthCheck
from openapi_client.models.basic_error import BasicError
from openapi_client.models.certificate import Certificate
from openapi_client.models.certificate_chain_for_as_available import CertificateChainForASAvailable
from openapi_client.models.certificate_chain_for_as_available_data import CertificateChainForASAvailableData
from openapi_client.models.certificate_chain_for_as_available_info import CertificateChainForASAvailableInfo
from openapi_client.models.certificate_chain_for_as_available_not_found import CertificateChainForASAvailableNotFound
from openapi_client.models.certificate_chain_for_as_available_wrapped import CertificateChainForASAvailableWrapped
from openapi_client.models.certificate_signing_request import CertificateSigningRequest
from openapi_client.models.certificate_subject import CertificateSubject
from openapi_client.models.chain import Chain
from openapi_client.models.chain_brief import ChainBrief
from openapi_client.models.check import Check
from openapi_client.models.check_summary import CheckSummary
from openapi_client.models.config import Config
from openapi_client.models.config_advanced import ConfigAdvanced
from openapi_client.models.config_advanced_service_customization import ConfigAdvancedServiceCustomization
from openapi_client.models.config_bgp import ConfigBgp
from openapi_client.models.config_bgp_global import ConfigBgpGlobal
from openapi_client.models.config_bgp_neighbor import ConfigBgpNeighbor
from openapi_client.models.config_bgp_neighbor_bfd import ConfigBgpNeighborBfd
from openapi_client.models.config_bgp_neighbor_timers import ConfigBgpNeighborTimers
from openapi_client.models.config_bgp_neighbor_transport import ConfigBgpNeighborTransport
from openapi_client.models.config_cluster import ConfigCluster
from openapi_client.models.config_cluster_features import ConfigClusterFeatures
from openapi_client.models.config_cluster_peer import ConfigClusterPeer
from openapi_client.models.config_cluster_peer_features import ConfigClusterPeerFeatures
from openapi_client.models.config_cluster_peer_scion import ConfigClusterPeerScion
from openapi_client.models.config_cluster_peer_scion_as import ConfigClusterPeerScionAS
from openapi_client.models.config_cluster_peer_scion_as_control import ConfigClusterPeerScionASControl
from openapi_client.models.config_cluster_peer_scion_as_neighbor import ConfigClusterPeerScionASNeighbor
from openapi_client.models.config_cluster_peer_scion_as_neighbor_interface import ConfigClusterPeerScionASNeighborInterface
from openapi_client.models.config_cluster_peer_scion_tunneling import ConfigClusterPeerScionTunneling
from openapi_client.models.config_cluster_peer_scion_tunneling_endpoint import ConfigClusterPeerScionTunnelingEndpoint
from openapi_client.models.config_cluster_peer_scion_tunneling_endpoint_allowed_interfaces import ConfigClusterPeerScionTunnelingEndpointAllowedInterfaces
from openapi_client.models.config_cluster_peer_synchronization import ConfigClusterPeerSynchronization
from openapi_client.models.config_cluster_synchronization import ConfigClusterSynchronization
from openapi_client.models.config_experiments import ConfigExperiments
from openapi_client.models.config_experiments_feature import ConfigExperimentsFeature
from openapi_client.models.config_firewall import ConfigFirewall
from openapi_client.models.config_firewall_table import ConfigFirewallTable
from openapi_client.models.config_firewall_table_chain import ConfigFirewallTableChain
from openapi_client.models.config_firewall_table_chain_rule import ConfigFirewallTableChainRule
from openapi_client.models.config_firewall_table_counter import ConfigFirewallTableCounter
from openapi_client.models.config_get_response_json import ConfigGetResponseJson
from openapi_client.models.config_interfaces import ConfigInterfaces
from openapi_client.models.config_interfaces_bond import ConfigInterfacesBond
from openapi_client.models.config_interfaces_bond_gateway import ConfigInterfacesBondGateway
from openapi_client.models.config_interfaces_bond_neighbor import ConfigInterfacesBondNeighbor
from openapi_client.models.config_interfaces_bond_route import ConfigInterfacesBondRoute
from openapi_client.models.config_interfaces_bond_vrrp import ConfigInterfacesBondVrrp
from openapi_client.models.config_interfaces_ethernet import ConfigInterfacesEthernet
from openapi_client.models.config_interfaces_ethernet_gateway import ConfigInterfacesEthernetGateway
from openapi_client.models.config_interfaces_ethernet_neighbor import ConfigInterfacesEthernetNeighbor
from openapi_client.models.config_interfaces_ethernet_route import ConfigInterfacesEthernetRoute
from openapi_client.models.config_interfaces_ethernet_vpp import ConfigInterfacesEthernetVpp
from openapi_client.models.config_interfaces_ethernet_vrrp import ConfigInterfacesEthernetVrrp
from openapi_client.models.config_interfaces_loopback import ConfigInterfacesLoopback
from openapi_client.models.config_interfaces_virtual_function import ConfigInterfacesVirtualFunction
from openapi_client.models.config_interfaces_virtual_function_gateway import ConfigInterfacesVirtualFunctionGateway
from openapi_client.models.config_interfaces_virtual_function_neighbor import ConfigInterfacesVirtualFunctionNeighbor
from openapi_client.models.config_interfaces_virtual_function_route import ConfigInterfacesVirtualFunctionRoute
from openapi_client.models.config_interfaces_virtual_function_vrrp import ConfigInterfacesVirtualFunctionVrrp
from openapi_client.models.config_interfaces_vlan import ConfigInterfacesVlan
from openapi_client.models.config_interfaces_vlan_gateway import ConfigInterfacesVlanGateway
from openapi_client.models.config_interfaces_vlan_neighbor import ConfigInterfacesVlanNeighbor
from openapi_client.models.config_interfaces_vlan_route import ConfigInterfacesVlanRoute
from openapi_client.models.config_interfaces_vlan_vrrp import ConfigInterfacesVlanVrrp
from openapi_client.models.config_interfaces_wireguard import ConfigInterfacesWireguard
from openapi_client.models.config_interfaces_wireguard_gateway import ConfigInterfacesWireguardGateway
from openapi_client.models.config_interfaces_wireguard_peer import ConfigInterfacesWireguardPeer
from openapi_client.models.config_interfaces_wireguard_route import ConfigInterfacesWireguardRoute
from openapi_client.models.config_management import ConfigManagement
from openapi_client.models.config_management_api import ConfigManagementApi
from openapi_client.models.config_management_api_basic_auth import ConfigManagementApiBasicAuth
from openapi_client.models.config_management_api_basic_auth_user import ConfigManagementApiBasicAuthUser
from openapi_client.models.config_management_api_listener import ConfigManagementApiListener
from openapi_client.models.config_management_api_oauth import ConfigManagementApiOauth
from openapi_client.models.config_management_api_oauth_identity_provider import ConfigManagementApiOauthIdentityProvider
from openapi_client.models.config_management_api_oauth_role import ConfigManagementApiOauthRole
from openapi_client.models.config_management_api_oauth_token_verification_key import ConfigManagementApiOauthTokenVerificationKey
from openapi_client.models.config_management_remote_repository import ConfigManagementRemoteRepository
from openapi_client.models.config_management_remote_repository_cloudsmith import ConfigManagementRemoteRepositoryCloudsmith
from openapi_client.models.config_management_ssh import ConfigManagementSsh
from openapi_client.models.config_management_ssh_user import ConfigManagementSshUser
from openapi_client.models.config_management_ssh_user_ssh_key import ConfigManagementSshUserSshKey
from openapi_client.models.config_management_telemetry import ConfigManagementTelemetry
from openapi_client.models.config_management_telemetry_flow_metrics import ConfigManagementTelemetryFlowMetrics
from openapi_client.models.config_management_telemetry_labels import ConfigManagementTelemetryLabels
from openapi_client.models.config_management_telemetry_logging import ConfigManagementTelemetryLogging
from openapi_client.models.config_management_telemetry_logging_loki import ConfigManagementTelemetryLoggingLoki
from openapi_client.models.config_management_telemetry_logging_loki_basic_auth import ConfigManagementTelemetryLoggingLokiBasicAuth
from openapi_client.models.config_management_telemetry_logging_loki_tls_config import ConfigManagementTelemetryLoggingLokiTlsConfig
from openapi_client.models.config_metadata import ConfigMetadata
from openapi_client.models.config_nat import ConfigNat
from openapi_client.models.config_nat_snat import ConfigNatSnat
from openapi_client.models.config_post_response_json import ConfigPostResponseJson
from openapi_client.models.config_put400_response import ConfigPut400Response
from openapi_client.models.config_put_request import ConfigPutRequest
from openapi_client.models.config_put_response_json import ConfigPutResponseJson
from openapi_client.models.config_scion import ConfigSCION
from openapi_client.models.config_scionas import ConfigSCIONAS
from openapi_client.models.config_scionasca_service import ConfigSCIONASCAService
from openapi_client.models.config_scionasca_service_anapaya_vault import ConfigSCIONASCAServiceAnapayaVault
from openapi_client.models.config_scionasca_service_anapaya_vault_credentials import ConfigSCIONASCAServiceAnapayaVaultCredentials
from openapi_client.models.config_scionasca_service_anapaya_vault_validation import ConfigSCIONASCAServiceAnapayaVaultValidation
from openapi_client.models.config_scionasca_service_external import ConfigSCIONASCAServiceExternal
from openapi_client.models.config_scionascppki import ConfigSCIONASCPPKI
from openapi_client.models.config_scionascppki_issuer import ConfigSCIONASCPPKIIssuer
from openapi_client.models.config_scionas_control import ConfigSCIONASControl
from openapi_client.models.config_scionas_details import ConfigSCIONASDetails
from openapi_client.models.config_scionas_neighbor import ConfigSCIONASNeighbor
from openapi_client.models.config_scionas_neighbor_interface import ConfigSCIONASNeighborInterface
from openapi_client.models.config_scionas_neighbor_interface_bfd import ConfigSCIONASNeighborInterfaceBFD
from openapi_client.models.config_scionas_neighbor_interface_remote import ConfigSCIONASNeighborInterfaceRemote
from openapi_client.models.config_scionas_router import ConfigSCIONASRouter
from openapi_client.models.config_scion_synchronization import ConfigSCIONSynchronization
from openapi_client.models.config_scion_tunneling import ConfigScionTunneling
from openapi_client.models.config_scion_tunneling_domain import ConfigScionTunnelingDomain
from openapi_client.models.config_scion_tunneling_domain_prefixes import ConfigScionTunnelingDomainPrefixes
from openapi_client.models.config_scion_tunneling_domain_prefixes_accept_filter_entry import ConfigScionTunnelingDomainPrefixesAcceptFilterEntry
from openapi_client.models.config_scion_tunneling_domain_prefixes_announce_filter_entry import ConfigScionTunnelingDomainPrefixesAnnounceFilterEntry
from openapi_client.models.config_scion_tunneling_domain_remote_matcher import ConfigScionTunnelingDomainRemoteMatcher
from openapi_client.models.config_scion_tunneling_domain_traffic_policy import ConfigScionTunnelingDomainTrafficPolicy
from openapi_client.models.config_scion_tunneling_domain_traffic_policy_failover_sequence_entry import ConfigScionTunnelingDomainTrafficPolicyFailoverSequenceEntry
from openapi_client.models.config_scion_tunneling_endpoint import ConfigScionTunnelingEndpoint
from openapi_client.models.config_scion_tunneling_endpoint_allowed_interfaces import ConfigScionTunnelingEndpointAllowedInterfaces
from openapi_client.models.config_scion_tunneling_path_filter import ConfigScionTunnelingPathFilter
from openapi_client.models.config_scion_tunneling_remote import ConfigScionTunnelingRemote
from openapi_client.models.config_scion_tunneling_static_announcement import ConfigScionTunnelingStaticAnnouncement
from openapi_client.models.config_scion_tunneling_static_announcement_next_hop_tracking import ConfigScionTunnelingStaticAnnouncementNextHopTracking
from openapi_client.models.config_scion_tunneling_traffic_matcher import ConfigScionTunnelingTrafficMatcher
from openapi_client.models.config_service_customization_response_json import ConfigServiceCustomizationResponseJson
from openapi_client.models.config_system import ConfigSystem
from openapi_client.models.config_system_dns import ConfigSystemDns
from openapi_client.models.config_system_dns_servers import ConfigSystemDnsServers
from openapi_client.models.config_system_kernel import ConfigSystemKernel
from openapi_client.models.config_system_ntp import ConfigSystemNtp
from openapi_client.models.config_system_ntp_servers import ConfigSystemNtpServers
from openapi_client.models.config_system_resources import ConfigSystemResources
from openapi_client.models.config_system_resources_service_limit import ConfigSystemResourcesServiceLimit
from openapi_client.models.config_system_vpp import ConfigSystemVpp
from openapi_client.models.config_system_vpp_buffers import ConfigSystemVppBuffers
from openapi_client.models.config_system_vpp_connection import ConfigSystemVppConnection
from openapi_client.models.config_system_vpp_connection_health_check import ConfigSystemVppConnectionHealthCheck
from openapi_client.models.config_system_vpp_cpu import ConfigSystemVppCpu
from openapi_client.models.config_system_vpp_tun import ConfigSystemVppTun
from openapi_client.models.cppki_certificate_blob_get_response_json import CppkiCertificateBlobGetResponseJson
from openapi_client.models.cppki_certificate_get_response_json import CppkiCertificateGetResponseJson
from openapi_client.models.cppki_certificates_get_response_json import CppkiCertificatesGetResponseJson
from openapi_client.models.cppki_certificates_post_response_json import CppkiCertificatesPostResponseJson
from openapi_client.models.cppki_certificates_renew_post_request import CppkiCertificatesRenewPostRequest
from openapi_client.models.cppki_certificates_request_post_request import CppkiCertificatesRequestPostRequest
from openapi_client.models.cppki_csr_blob_get_response_json import CppkiCsrBlobGetResponseJson
from openapi_client.models.cppki_csr_get_response_json import CppkiCsrGetResponseJson
from openapi_client.models.cppki_csrs_get_response_json import CppkiCsrsGetResponseJson
from openapi_client.models.cppki_csrs_post_response_json import CppkiCsrsPostResponseJson
from openapi_client.models.cppki_trc_blob_get_response_json import CppkiTrcBlobGetResponseJson
from openapi_client.models.cppki_trc_get_response_json import CppkiTrcGetResponseJson
from openapi_client.models.cppki_trcs_bundle_post_response_json import CppkiTrcsBundlePostResponseJson
from openapi_client.models.cppki_trcs_get_response_json import CppkiTrcsGetResponseJson
from openapi_client.models.cppki_trcs_post_response_json import CppkiTrcsPostResponseJson
from openapi_client.models.csr_info import CsrInfo
from openapi_client.models.debug_cluster_peer import DebugClusterPeer
from openapi_client.models.debug_cluster_status import DebugClusterStatus
from openapi_client.models.debug_notify_status_json import DebugNotifyStatusJson
from openapi_client.models.debug_scion_interface import DebugScionInterface
from openapi_client.models.debug_scion_interfaces import DebugScionInterfaces
from openapi_client.models.debug_scion_sibling_interface import DebugScionSiblingInterface
from openapi_client.models.debug_service_groups_restart_response_json import DebugServiceGroupsRestartResponseJson
from openapi_client.models.debug_services_group import DebugServicesGroup
from openapi_client.models.debug_services_response_json import DebugServicesResponseJson
from openapi_client.models.domain_exchanges_ip_prefixes import DomainExchangesIPPrefixes
from openapi_client.models.domain_exchanges_ip_prefixes_data import DomainExchangesIPPrefixesData
from openapi_client.models.domain_exchanges_ip_prefixes_wrapped import DomainExchangesIPPrefixesWrapped
from openapi_client.models.domain_has_paths_to_remote import DomainHasPathsToRemote
from openapi_client.models.domain_has_paths_to_remote_data import DomainHasPathsToRemoteData
from openapi_client.models.domain_has_paths_to_remote_wrapped import DomainHasPathsToRemoteWrapped
from openapi_client.models.domain_has_reachable_remote_gateways import DomainHasReachableRemoteGateways
from openapi_client.models.domain_has_reachable_remote_gateways_data import DomainHasReachableRemoteGatewaysData
from openapi_client.models.domain_has_reachable_remote_gateways_wrapped import DomainHasReachableRemoteGatewaysWrapped
from openapi_client.models.domain_remote_gateway import DomainRemoteGateway
from openapi_client.models.domain_traffic_policy_failover_sequence import DomainTrafficPolicyFailoverSequence
from openapi_client.models.domain_traffic_policy_has_paths import DomainTrafficPolicyHasPaths
from openapi_client.models.domain_traffic_policy_has_paths_data import DomainTrafficPolicyHasPathsData
from openapi_client.models.domain_traffic_policy_has_paths_wrapped import DomainTrafficPolicyHasPathsWrapped
from openapi_client.models.encryption_mode import EncryptionMode
from openapi_client.models.error_base import ErrorBase
from openapi_client.models.external_ca_available import ExternalCAAvailable
from openapi_client.models.external_ca_available_data import ExternalCAAvailableData
from openapi_client.models.external_ca_available_wrapped import ExternalCAAvailableWrapped
from openapi_client.models.external_interface_up import ExternalInterfaceUp
from openapi_client.models.external_interface_up_data import ExternalInterfaceUpData
from openapi_client.models.external_interface_up_wrapped import ExternalInterfaceUpWrapped
from openapi_client.models.feature_mapping import FeatureMapping
from openapi_client.models.feature_set_mapping import FeatureSetMapping
from openapi_client.models.fetch_status import FetchStatus
from openapi_client.models.firewall_chain import FirewallChain
from openapi_client.models.firewall_chain_json import FirewallChainJson
from openapi_client.models.firewall_counter import FirewallCounter
from openapi_client.models.firewall_rule import FirewallRule
from openapi_client.models.firewall_table import FirewallTable
from openapi_client.models.firewall_table_family import FirewallTableFamily
from openapi_client.models.firewall_table_json import FirewallTableJson
from openapi_client.models.firewalls_json import FirewallsJson
from openapi_client.models.health import Health
from openapi_client.models.health_check import HealthCheck
from openapi_client.models.health_component import HealthComponent
from openapi_client.models.health_get_response_json import HealthGetResponseJson
from openapi_client.models.health_response import HealthResponse
from openapi_client.models.health_status import HealthStatus
from openapi_client.models.health_summary import HealthSummary
from openapi_client.models.health_summary_response import HealthSummaryResponse
from openapi_client.models.hop import Hop
from openapi_client.models.install_status import InstallStatus
from openapi_client.models.keys import Keys
from openapi_client.models.lan_features import LANFeatures
from openapi_client.models.lan_stats import LanStats
from openapi_client.models.lan_stats_gateway import LanStatsGateway
from openapi_client.models.license_payload_json import LicensePayloadJson
from openapi_client.models.license_request_data import LicenseRequestData
from openapi_client.models.license_request_get_response_json import LicenseRequestGetResponseJson
from openapi_client.models.license_status_get_response_json import LicenseStatusGetResponseJson
from openapi_client.models.license_type import LicenseType
from openapi_client.models.license_validity import LicenseValidity
from openapi_client.models.licenses_get_response_json import LicensesGetResponseJson
from openapi_client.models.link_relationship import LinkRelationship
from openapi_client.models.link_state import LinkState
from openapi_client.models.management_features import ManagementFeatures
from openapi_client.models.max_or_unlimited import MaxOrUnlimited
from openapi_client.models.meta_health_check import MetaHealthCheck
from openapi_client.models.network_interface import NetworkInterface
from openapi_client.models.network_interfaces import NetworkInterfaces
from openapi_client.models.network_physical_interfaces_get_response_json import NetworkPhysicalInterfacesGetResponseJson
from openapi_client.models.network_route import NetworkRoute
from openapi_client.models.network_routes import NetworkRoutes
from openapi_client.models.network_wireguards_get_response_json import NetworkWireguardsGetResponseJson
from openapi_client.models.network_wireguards_interface_get_response_json import NetworkWireguardsInterfaceGetResponseJson
from openapi_client.models.package_info import PackageInfo
from openapi_client.models.path import Path
from openapi_client.models.physical_interface import PhysicalInterface
from openapi_client.models.ping_run import PingRun
from openapi_client.models.ping_statistics import PingStatistics
from openapi_client.models.ping_summary import PingSummary
from openapi_client.models.ping_update import PingUpdate
from openapi_client.models.problem import Problem
from openapi_client.models.product_tier_features import ProductTierFeatures
from openapi_client.models.public_key import PublicKey
from openapi_client.models.scion_features import SCIONFeatures
from openapi_client.models.schemas_health import SchemasHealth
from openapi_client.models.schemas_validity import SchemasValidity
from openapi_client.models.scion_interface_endpoint import ScionInterfaceEndpoint
from openapi_client.models.scion_path import ScionPath
from openapi_client.models.scion_path_hop import ScionPathHop
from openapi_client.models.scion_path_performance_metrics import ScionPathPerformanceMetrics
from openapi_client.models.scion_path_with_metrics import ScionPathWithMetrics
from openapi_client.models.scion_tunneling_discovery import ScionTunnelingDiscovery
from openapi_client.models.scion_tunneling_discovery_peer import ScionTunnelingDiscoveryPeer
from openapi_client.models.scion_tunneling_discovery_session import ScionTunnelingDiscoverySession
from openapi_client.models.scion_tunneling_domain_config import ScionTunnelingDomainConfig
from openapi_client.models.scion_tunneling_domain_config_prefixes import ScionTunnelingDomainConfigPrefixes
from openapi_client.models.scion_tunneling_domains_response_json import ScionTunnelingDomainsResponseJson
from openapi_client.models.scion_tunneling_failover_sequence_entry import ScionTunnelingFailoverSequenceEntry
from openapi_client.models.scion_tunneling_isd_as_filter import ScionTunnelingIsdAsFilter
from openapi_client.models.scion_tunneling_path_data_json import ScionTunnelingPathDataJson
from openapi_client.models.scion_tunneling_paths_search_post_request_json import ScionTunnelingPathsSearchPostRequestJson
from openapi_client.models.scion_tunneling_paths_search_response_json import ScionTunnelingPathsSearchResponseJson
from openapi_client.models.scion_tunneling_prefixes_filter import ScionTunnelingPrefixesFilter
from openapi_client.models.scion_tunneling_routing_chain import ScionTunnelingRoutingChain
from openapi_client.models.scion_tunneling_sgrp_domain import ScionTunnelingSGRPDomain
from openapi_client.models.scion_tunneling_sgrp_domains import ScionTunnelingSGRPDomains
from openapi_client.models.scion_tunneling_sgrp_local_prefixes import ScionTunnelingSGRPLocalPrefixes
from openapi_client.models.scion_tunneling_sgrp_local_prefixes_bgp import ScionTunnelingSGRPLocalPrefixesBGP
from openapi_client.models.scion_tunneling_sgrp_local_prefixes_json import ScionTunnelingSGRPLocalPrefixesJSON
from openapi_client.models.scion_tunneling_sgrp_local_prefixes_static import ScionTunnelingSGRPLocalPrefixesStatic
from openapi_client.models.scion_tunneling_sgrp_local_prefixes_static_probed import ScionTunnelingSGRPLocalPrefixesStaticProbed
from openapi_client.models.scion_tunneling_sgrp_peer import ScionTunnelingSGRPPeer
from openapi_client.models.scion_tunneling_sgrp_peers import ScionTunnelingSGRPPeers
from openapi_client.models.scion_tunneling_session import ScionTunnelingSession
from openapi_client.models.scion_tunneling_session_path import ScionTunnelingSessionPath
from openapi_client.models.scion_tunneling_summary import ScionTunnelingSummary
from openapi_client.models.scion_tunneling_traffic_matcher import ScionTunnelingTrafficMatcher
from openapi_client.models.scion_tunneling_traffic_policy import ScionTunnelingTrafficPolicy
from openapi_client.models.service_type import ServiceType
from openapi_client.models.showpaths_run import ShowpathsRun
from openapi_client.models.sibling_interface_up import SiblingInterfaceUp
from openapi_client.models.sibling_interface_up_data import SiblingInterfaceUpData
from openapi_client.models.sibling_interface_up_wrapped import SiblingInterfaceUpWrapped
from openapi_client.models.signature import Signature
from openapi_client.models.signatures import Signatures
from openapi_client.models.software_install_get_response_json import SoftwareInstallGetResponseJson
from openapi_client.models.software_install_post_request_json import SoftwareInstallPostRequestJson
from openapi_client.models.software_install_post_response_json import SoftwareInstallPostResponseJson
from openapi_client.models.software_installed_get_response_json import SoftwareInstalledGetResponseJson
from openapi_client.models.software_license_features_put_request import SoftwareLicenseFeaturesPutRequest
from openapi_client.models.software_licenses_post_request import SoftwareLicensesPostRequest
from openapi_client.models.software_package_delete_response_json import SoftwarePackageDeleteResponseJson
from openapi_client.models.software_package_fetch import SoftwarePackageFetch
from openapi_client.models.software_package_fetch_get_response_json import SoftwarePackageFetchGetResponseJson
from openapi_client.models.software_package_fetch_post_request_json import SoftwarePackageFetchPostRequestJson
from openapi_client.models.software_package_fetch_post_response_json import SoftwarePackageFetchPostResponseJson
from openapi_client.models.software_package_get_response_json import SoftwarePackageGetResponseJson
from openapi_client.models.software_package_install_info import SoftwarePackageInstallInfo
from openapi_client.models.software_packages_get_response_json import SoftwarePackagesGetResponseJson
from openapi_client.models.software_packages_post_response_json import SoftwarePackagesPostResponseJson
from openapi_client.models.status import Status
from openapi_client.models.trc import TRC
from openapi_client.models.trc_for_local_isd_available import TRCForLocalISDAvailable
from openapi_client.models.trc_for_local_isd_available_data import TRCForLocalISDAvailableData
from openapi_client.models.trc_for_local_isd_available_in_daemon import TRCForLocalISDAvailableInDaemon
from openapi_client.models.trc_for_local_isd_available_in_daemon_data import TRCForLocalISDAvailableInDaemonData
from openapi_client.models.trc_for_local_isd_available_in_daemon_wrapped import TRCForLocalISDAvailableInDaemonWrapped
from openapi_client.models.trc_for_local_isd_available_info import TRCForLocalISDAvailableInfo
from openapi_client.models.trc_for_local_isd_available_not_found import TRCForLocalISDAvailableNotFound
from openapi_client.models.trc_for_local_isd_available_wrapped import TRCForLocalISDAvailableWrapped
from openapi_client.models.trcid import TRCID
from openapi_client.models.trc_info import TRCInfo
from openapi_client.models.tier_mapping import TierMapping
from openapi_client.models.tools_scion_ping_post_request import ToolsScionPingPostRequest
from openapi_client.models.tools_scion_ping_post_response_json import ToolsScionPingPostResponseJson
from openapi_client.models.tools_scion_showpaths_post_request import ToolsScionShowpathsPostRequest
from openapi_client.models.tools_scion_showpaths_post_response_json import ToolsScionShowpathsPostResponseJson
from openapi_client.models.tools_scion_traceroute_post_request import ToolsScionTraceroutePostRequest
from openapi_client.models.tools_scion_traceroute_post_response_json import ToolsScionTraceroutePostResponseJson
from openapi_client.models.traceroute_hop_info import TracerouteHopInfo
from openapi_client.models.traceroute_run import TracerouteRun
from openapi_client.models.traceroute_summary import TracerouteSummary
from openapi_client.models.tunneling_features import TunnelingFeatures
from openapi_client.models.validation_error import ValidationError
from openapi_client.models.validation_violation import ValidationViolation
from openapi_client.models.validity import Validity
from openapi_client.models.with_service_info import WithServiceInfo
